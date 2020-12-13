import torch
import torchvision
import torch.nn.functional as F
import torch.utils.model_zoo as model_zoo
import torch.nn as nn

from module.sequential import Sequential
from module.linear import Linear
from module.relu import ReLU
from module.convolution import _ConvNd
from module.pool import _MaxPoolNd
from module.module import Module
from module.convolution import Conv2d
from module.pool import MaxPool2d
from module.arguments import get_args
from module.batchnorm import BatchNorm2d
from module.adaptiveAvgPool2d import AdaptiveAvgPool2d

import torchvision 

import os
args = get_args()

__all__ = ['ResNet', 'resnet18', 'resnet34', 'resnet50', 'resnet101',
           'resnet152']


model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
}



def conv3x3(in_planes, out_planes, stride=1):
    """3x3 convolution with padding"""
    return Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)


def conv1x1(in_planes, out_planes, stride=1):
    """1x1 convolution"""
    return Conv2d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)


class BasicBlock(Module):
    expansion = 1
        
    def __init__(self, inplanes, planes, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = BatchNorm2d(planes)
        self.relu1 = ReLU(inplace=False)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = BatchNorm2d(planes)
        self.relu2 = ReLU(inplace=False)
        self.downsample = downsample
        if downsample is not None and len(downsample) != 0:
            self.down_conv3 = downsample[0]
            self.down_bn3 = downsample[1]
        self.stride = stride


    def forward(self, x):

        # For foward output, For LRP, save layers in list 'layers'
        layers = []
        identity = x

        out = self.conv1(x)
        layers.append(self.conv1)
        
        out = self.bn1(out)
        layers.append(self.bn1)
        
        out = self.relu1(out)
        layers.append(self.relu1)

        out = self.conv2(out)
        layers.append(self.conv2)
        
        out = self.bn2(out)
        layers.append(self.bn2)

        if self.downsample is not None and len(self.downsample) != 0:
            identity = self.down_conv3(x)
            identity = self.down_bn3(identity)

        self.out = out
        out += identity
        out = self.relu2(out)
        layers.append(self.relu2)
        
        self.x = identity
        self.layers = layers

        return out
    
    def _simple_lrp(self, R, labels):
        lrp_var = args.r_method
        param=None
        
        for key, module in enumerate(reversed(self.layers)):
            R = module.lrp(R, labels, lrp_var, param)
            if key == 0 : 
                # Skip connection alpha beta
                out_p = torch.where(self.out<0, torch.zeros(1).cuda(), self.out)
                out_n = self.out - out_p

                x_p = torch.where(self.x<0, torch.zeros(1).cuda(), self.x)
                x_n = self.x - x_p

                Rout_p = (out_p/(out_p + x_p + 1e-12)) * R
                Rx_p = (x_p/(out_p + x_p + 1e-12)) * R

                Rout_n = (out_n/(out_p + x_n + 1e-12)) * R
                Rx_n = (x_n/(out_n + x_n + 1e-12)) * R

                self.Rout = (1-args.beta) * Rout_p + (args.beta * Rout_n)
                self.Rx = (1-args.beta) * Rx_p + (args.beta * Rx_n)

                R = self.Rout

                if self.downsample is not None and len(self.downsample) != 0:
                    Rx = self.Rx
                    for key, module in enumerate(reversed(self.downsample)):
                        Rx = module.lrp(Rx, labels, lrp_var, param)
                    self.Rx = Rx

        return R + self.Rx

        
    def _composite_lrp(self, R, labels):
        return self._simple_lrp(R, labels)
    
    def _grad_cam(self, dx, requires_activation):
        for key, module in enumerate(reversed(self.layers)):
            # x: feature map, dx: dL/dx
            dx, x = module.grad_cam(dx, requires_activation)
            if key == 0 : # when identity order, after last relu, +x used only downsample is None
                dx_iden = dx
                if self.downsample is not None:
                    for key, module in enumerate(reversed(self.downsample)):
                        # x: feature map, dx: dL/dx
                        dx_iden, x = module.grad_cam(dx_iden, requires_activation)

        # Add dx_iden for block that has identity layer
        dx = dx + dx_iden
 
        if requires_activation:
            return dx, x

        return dx, None
    
    
        

class Bottleneck(Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = conv1x1(inplanes, planes)
        self.bn1 = BatchNorm2d(planes)
        self.conv2 = conv3x3(planes, planes, stride)
        self.bn2 = BatchNorm2d(planes)
        self.conv3 = conv1x1(planes, planes * self.expansion)
        self.bn3 = BatchNorm2d(planes * self.expansion)
        self.relu1 = ReLU(inplace=False)
        self.relu2 = ReLU(inplace=False)
        self.relu3 = ReLU(inplace=False)
        self.downsample = downsample
        if downsample is not None and len(downsample) != 0:
            self.down_conv4 = downsample[0]
            self.down_bn4 = downsample[1]
        self.stride = stride

    def forward(self, x):
        layers = []
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu1(out)
        layers.append(self.conv1)
        layers.append(self.bn1)
        layers.append(self.relu1)
        
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu2(out)
        layers.append(self.conv2)
        layers.append(self.bn2)
        layers.append(self.relu2)
        
        out = self.conv3(out)
        out = self.bn3(out)
        layers.append(self.conv3)
        layers.append(self.bn3)
        
        if self.downsample is not None and len(self.downsample) != 0:
            identity = self.down_conv4(x)
            identity = self.down_bn4(identity)
            
        self.out = out
        out += identity
        out = self.relu3(out)
        layers.append(self.relu3)

        self.x = identity
        self.layers = layers
        return out
                      
    
    def _simple_lrp(self, R, labels):
        lrp_var = args.r_method
        param=None
        
        for key, module in enumerate(reversed(self.layers)):
            R = module.lrp(R, labels, lrp_var, param)
            if key == 0 : # when identity order, after last relu

                # Skip connection alpha beta
                out_p = torch.where(self.out<0, torch.zeros(1).cuda(), self.out)
                out_n = self.out - out_p

                x_p = torch.where(self.x<0, torch.zeros(1).cuda(), self.x)
                x_n = self.x - x_p

                Rout_p = (out_p/(out_p + x_p + 1e-12)) * R
                Rx_p = (x_p/(out_p + x_p + 1e-12)) * R

                Rout_n = (out_n/(out_p + x_n + 1e-12)) * R
                Rx_n = (x_n/(out_n + x_n + 1e-12)) * R

                self.Rout = (1-args.beta) * Rout_p + (args.beta * Rout_n)
                self.Rx = (1-args.beta) * Rx_p + (args.beta * Rx_n)

                R = self.Rout

                if self.downsample is not None and len(self.downsample) != 0:
                    Rx = self.Rx
                    for key, module in enumerate(reversed(self.downsample)):
                        Rx = module.lrp(Rx, labels, lrp_var, param)
                    self.Rx = Rx

        return R + self.Rx
        
    def _composite_lrp(self, R, labels):
        return self._simple_lrp(R, labels)
    
    def _grad_cam(self, dx, requires_activation):
        for key, module in enumerate(reversed(self.layers)):
            # x: feature map, dx: dL/dx
            dx, x = module.grad_cam(dx, requires_activation)
            if key == 0 : # when identity order, after last relu, +x used only downsample is None
                dx_iden = dx
                if self.downsample is not None:
                    for key, module in enumerate(reversed(self.downsample)):
                        # x: feature map, dx: dL/dx
                        dx_iden, x = module.grad_cam(dx_iden, requires_activation)

        # Add dx_iden for block that has identity layer
        dx = dx + dx_iden
 
        if requires_activation:
            return dx, x

        return dx, None


class ResNet(Module):

    def __init__(self, block, layers, num_classes=1000, zero_init_residual=False):
        super(ResNet, self).__init__()
        self.inplanes = 64
        self.conv1 = Conv2d(3, 64, kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = BatchNorm2d(64)
        self.relu = ReLU(inplace=False)
        self.maxpool = MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        self.avgpool = AdaptiveAvgPool2d((1, 1))
        self.fc = Linear(512 * block.expansion, num_classes, whichScore = args.whichScore,lastLayer=True)

        for m in self.modules():
            if isinstance(m, Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        # Zero-initialize the last BN in each residual branch,
        # so that the residual branch starts with zeros, and each residual block behaves like an identity.
        # This improves the model by 0.2~0.3% according to https://arxiv.org/abs/1706.02677
        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, Bottleneck):
                    nn.init.constant_(m.bn3.weight, 0)
                elif isinstance(m, BasicBlock):
                    nn.init.constant_(m.bn2.weight, 0)

    def _make_layer(self, block, planes, blocks, stride=1):
        downsample = []
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample=downsample+[conv1x1(self.inplanes, planes * block.expansion, stride), BatchNorm2d(planes * block.expansion)]


        layers = []
        layers = layers + [block(self.inplanes, planes, stride, downsample)]
        self.inplanes = planes * block.expansion
        for _ in range(1, blocks):
            layers = layers + [block(self.inplanes, planes)]
        
        return layers

    
    def forward(self):
        layers = []
        layers.append(self.conv1)
        layers.append(self.bn1)
        layers.append(self.relu)
        layers.append(self.maxpool)
        layers = layers + self.layer1
        layers = layers + self.layer2
        layers = layers + self.layer3
        layers = layers + self.layer4
        layers.append(self.avgpool) 
        layers.append(self.fc)
                      
        return Sequential(*layers)


def resnet18(pretrained=False,pretrained_path=None, **kwargs):
    """Constructs a ResNet-18 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2], **kwargs).forward()
    if pretrained:
        if pretrained_path == None :
            dummy_model = torchvision.models.resnet18(pretrained=True)

            for key1, key2 in zip(model.state_dict().keys(), dummy_model.state_dict().keys()):
                if model.state_dict()[key1].shape == torch.tensor(1).shape:
                    model.state_dict()[key1] = dummy_model.state_dict()[key2]
                else:
                    model.state_dict()[key1][:] = dummy_model.state_dict()[key2][:]
        else:
            model.load_state_dict(torch.load(pretrained_path))
    return model


def resnet34(pretrained=False, pretrained_path=None,**kwargs):
    """Constructs a ResNet-34 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [3, 4, 6, 3], **kwargs).forward()
    if pretrained:
        if pretrained_path == None :
            dummy_model = torchvision.models.resnet34(pretrained=True)

            for key1, key2 in zip(model.state_dict().keys(), dummy_model.state_dict().keys()):
                if model.state_dict()[key1].shape == torch.tensor(1).shape:
                    model.state_dict()[key1] = dummy_model.state_dict()[key2]
                else:
                    model.state_dict()[key1][:] = dummy_model.state_dict()[key2][:]
        else:
            model.load_state_dict(torch.load(pretrained_path))
    return model


def resnet50(pretrained=False, pretrained_path=None,**kwargs):
    """Constructs a ResNet-50 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 6, 3], **kwargs).forward()
    if pretrained:
        if pretrained_path == None :
            dummy_model = torchvision.models.resnet50(pretrained=True)

            k1 = model.state_dict().keys()
            k2 = dummy_model.state_dict().keys()
            for key1, key2 in zip(model.state_dict().keys(), dummy_model.state_dict().keys()):
                if model.state_dict()[key1].shape == torch.tensor(1).shape:
                    model.state_dict()[key1] = dummy_model.state_dict()[key2]
                else:
                    model.state_dict()[key1][:] = dummy_model.state_dict()[key2][:]
        else:
            model.load_state_dict(torch.load(pretrained_path))
    return model


def resnet101(pretrained=False, pretrained_path=None,**kwargs):
    """Constructs a ResNet-101 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 23, 3], **kwargs).forward()
    if pretrained:
        if pretrained_path == None :
            dummy_model = torchvision.models.resnet101(pretrained=True)

            for key1, key2 in zip(model.state_dict().keys(), dummy_model.state_dict().keys()):
                if model.state_dict()[key1].shape == torch.tensor(1).shape:
                    model.state_dict()[key1] = dummy_model.state_dict()[key2]
                else:
                    model.state_dict()[key1][:] = dummy_model.state_dict()[key2][:]
        
        else:
            model.load_state_dict(torch.load(pretrained_path))
    return model


def resnet152(pretrained=False, **kwargs):
    """Constructs a ResNet-152 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 8, 36, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['resnet152']))
    return model
