#!/usr/bin/env python3
'''
    pytorch NN for learning MNIST models

    We're using the network from

    https://github.com/pytorch/examples/blob/master/mnist/main.py

    Because we're not trying to prove anything by writing our own. We just want
    something quick that is known to work.
'''
import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    """ from https://github.com/pytorch/examples/blob/master/mnist/main.py """
    def __init__(self, checkpoint_path=None):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

        if checkpoint_path is not None:
            ckpt = torch.load(checkpoint_path)
            self.load_state_dict(ckpt)
            self.eval()

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output
