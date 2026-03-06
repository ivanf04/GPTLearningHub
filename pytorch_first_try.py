import torch 
import torch.nn as nn

# x = torch.rand(5, 3)
# print(x)

# pyTorch uses tensor as primary data type, similar to a matrix/array 
# tensors can start any data type we want; they carry / store derivates under the hood 

# make a tensor of all ones 
a = torch.ones(3, 5)
# print(a)

# important functions in pytorch  sum() and mean()
# sum has argument axis, 0 corresponds to columns while 1 corresponds to rows 
sum = torch.sum(a, axis= 0)
# print(sum)

sum_rows = torch.sum(a, axis= 1)
# print(sum_rows)

# squeze() changes how the shape of the tensot is represented which is needed when pasing tensors as arguments to other functions 
# unsqueeze() does the opposite, it unsqueezeses or adds an extra demesion, dim is needed as an argument to specify index of additional demension 

b = torch.ones(5, 1)
print('print(b.shape) ', b.shape)  #outputs dimensions of the tensor
squeezed = torch.squeeze(b)
print('print(squeezed.shape) ', squeezed.shape)
print(b)
print('print(squeezed) ', squeezed)
print('print(torch.unsqueeze(b, 1))', torch.unsqueeze(b, 1))



