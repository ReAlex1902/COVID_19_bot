
import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(8, 64)
        self.layers = [nn.Linear(64, 64)] * 9
        self.fc12 = nn.Linear(64, 2)

    def return_one_number(self, result):
        """
        Helps to return not the number of prediction
        """
        CONSTANT = - 1.2             ## constant number to compare hthe prediction with
        # lst = torch.Tensor(lst)     ## transforming to pytorch tensor
        # result = self.forward(lst)      ##
        lst = [1 if elem[1] > CONSTANT else int(torch.argmax(elem)) for elem in result]    ## regulation of predictions
        return lst

    def forward(self, X):
        X = torch.Tensor(X)
        X = X.view(-1, 8).float()           ## preparing Tensor

        X = F.relu(self.fc1(X))
        for layer in self.layers:           ## predicting
            X = layer(X)
        X = self.fc12(X)
        result = F.log_softmax(X, dim = 1)           ## writing results using log_softmax

        return (self.return_one_number(result), result)     ## returning tuple with list of predictions and tensor of
                                                            ## log_softmax probabilities


def get_model(filename = "net.pt"):
    import pickle
    import torch
    model = torch.load(filename)
    return model
