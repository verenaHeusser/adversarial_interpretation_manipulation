import torch
cuda = torch.device('cuda') 

use_cuda = True
if use_cuda:
    dtype = torch.cuda.FloatTensor
else:
    dtype = torch.FloatTensor

x = torch.rand(2,2).type(dtype)