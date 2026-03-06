import torch 
import torch.nn as nn

# implementing NN in pytorch, modules in pytorch are the same as a model, inherits nn.module, you need to override forward method
# nn.linear as layers within our nearal networ, in feuatures = number of inputs, outfeatures is number of nodes in the layer 

# make NN with 4 input nodes, 1 hidden layers and 2 output nodes in output layer 
# inital hidden weights are "randomly" (probability distribution) chosen 

class MyModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.first_layer = nn.Linear(4,6)
        self.second_layer = nn.Linear(6,6)
        self.output_layrer = nn.Linear(6, 2)
    
    def forward(self, x):
        return self.output_layrer(self.second_layer(self.first_layer(x)))
    
model = MyModel()

example_datapoint = torch.randn(1,4)

print(model(example_datapoint))

# train model for some number of iternations 
# then we can use the model and get predictions 

