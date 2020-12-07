import torch
cuda = torch.device('cuda') 

use_cuda = True
if use_cuda:
    dtype = torch.cuda.FloatTensor
    print('fuck jei')
else:
    dtype = torch.FloatTensor

x = torch.rand(2,2).type(dtype)
# # RuntimeError: CUDA unknown error - this may be due to an incorrectly set up environment, e.g. changing env variable CUDA_VISIBLE_DEVICES after program start. Setting the available devices to be zero.

# import tensorflow as tf 
# if tf.test.gpu_device_name(): 
#     print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
# else:
#     print("Please install GPU version of TF")
