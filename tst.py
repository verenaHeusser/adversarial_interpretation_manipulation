# import torch
# cuda = torch.device('cuda') 

# use_cuda = True
# if use_cuda:
#     dtype = torch.cuda.FloatTensor
# else:
#     dtype = torch.FloatTensor

# x = torch.rand(2,2).type(dtype)



import tensorflow as tf 
if tf.test.gpu_device_name(): 
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
