import torch
import torchvision
from module.arguments import get_args
import torchvision.transforms as T
from torchvision import utils
from torchvision import transforms
import numpy as np


def dataloader(args, train=False, val=False, test=False, single=False):
    if train + val + test != 1:
        print("Only one of the loader should be True")
        # print(ERROR)

    # Change it to your ImageNet directory
    # train_dir = './../../../Interpretable/Data/ImageNet/Data/train'
    # val_dir = './../../../Interpretable/Data/ImageNet/Data/val'
    train_dir = "./../../../data/ILSVRC2012/train"
    val_dir = "./../../../data/ILSVRC2012/val"
    single_img_dir = "./../../../data/ILSVRC2012/single_test"

    normalize = transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))

    if train:
        train_dataset = torchvision.datasets.ImageFolder(
            train_dir,
            transform=transforms.Compose(
                [
                    transforms.RandomResizedCrop(224),
                    transforms.RandomHorizontalFlip(),
                    transforms.ToTensor(),
                    normalize,
                ]
            ),
        )

        train_loader = torch.utils.data.DataLoader(
            train_dataset, batch_size=args.batch_size, shuffle=True
        )
        return train_loader

    elif val or test:
        val_loader = torch.utils.data.DataLoader(
            torchvision.datasets.ImageFolder(
                val_dir,
                transforms.Compose(
                    [
                        transforms.Resize(256),
                        transforms.CenterCrop(224),
                        transforms.ToTensor(),
                        normalize,
                    ]
                ),
            ),
            batch_size=args.batch_size_test,
            shuffle=True,
            num_workers=args.num_workers,
            pin_memory=True,
        )
        return val_loader
    
    if single: 
        single_loader = torch.utils.data.DataLoader(
            torchvision.datasets.ImageFolder(
                single_img_dir,
                transforms.Compose(
                    [
                        transforms.Resize(256),
                        transforms.CenterCrop(224),
                        transforms.ToTensor(),
                        normalize,
                    ]
                ),
            ),
            batch_size=args.batch_size_test,
            shuffle=True,
            num_workers=args.num_workers,
            pin_memory=True,
        )
        return single_loader
    

def active_loader(args):
    
    dir = "./../../data/ILSVRC2012/targeted_dataset/"

    n1, n2 = args.class_c1, args.class_c2
    D_fool_data_dir = (
        dir
        + str(min(n1, n2))
        + "_"
        + str(max(n1, n2))
        + ".npy"
    )
    # c1_dir = "./../../../Interpretable/Data/Targeted_dataset/" + str(args.class_c1)
    # c2_dir = "./../../../Interpretable/Data/Targeted_dataset/" + str(args.class_c2)

    c1_dir = dir + str(args.class_c1)
    c2_dir = dir + str(args.class_c2)

    normalize = transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))

    # 2. Labeled dataset for training and validation
    D_fool_data = np.load(D_fool_data_dir)

    # normalization
    mean = np.array([0.485, 0.456, 0.406]).reshape(1, 3, 1, 1)
    std = np.array([0.229, 0.224, 0.225]).reshape(1, 3, 1, 1)
    x = (D_fool_data - mean) / std

    # numpy to dataset.
    x = torch.tensor(x, dtype=torch.float32)

    # Data loader
    D_fool_dataset = torch.utils.data.TensorDataset(x[100:1200])

    D_fool_loader = torch.utils.data.DataLoader(
        D_fool_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.num_workers,
        pin_memory=True,
    )

    val_dataset = torch.utils.data.TensorDataset(torch.cat((x[1200:1300], x[:100]), 0))

    val_loader = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=args.batch_size_test,
        shuffle=True,
        num_workers=args.num_workers,
        pin_memory=True,
    )

    c1_loader = torch.utils.data.DataLoader(
        torchvision.datasets.ImageFolder(
            c1_dir,
            transforms.Compose(
                [
                    transforms.Resize(256),
                    transforms.CenterCrop(224),
                    transforms.ToTensor(),
                    normalize,
                ]
            ),
        ),
        batch_size=16,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=True,
    )

    c2_loader = torch.utils.data.DataLoader(
        torchvision.datasets.ImageFolder(
            c2_dir,
            transforms.Compose(
                [
                    transforms.Resize(256),
                    transforms.CenterCrop(224),
                    transforms.ToTensor(),
                    normalize,
                ]
            ),
        ),
        batch_size=16,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=True,
    )

    return D_fool_loader, val_loader, c1_loader, c2_loader
