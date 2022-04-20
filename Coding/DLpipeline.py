"""
For this coding problem, we are about to achieve a deep learning
training pipeline (for example, in pytorch style), But we need to use
the finance data as following description:

Our input x in in shape of :
[number_of_stocks, time_steps, feature_size]
Our output y is in shape of :
[number_of_stocks, time_steps, 1]

The meaning of x could be the factors or signals
The meaning of y could be the rate of returns or any other predictions
If we predict y at time t, we can only use the information in 1, ..., t-1

Your goal is to: 
1. Generate pseudo data x and y for training
2. Define your own model (any model you can come up with)
3. Define loss function, optimizer, and realize training pipeline
4. Try to run the code

We will provide some Pytorch template for your coding.
The templates may occur some error, please be careful.
"""

import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

# ==================== Data generation ====================

class MyDataSet():
    def __init__(
        self,
        num_of_stocks: int,
        time_steps: int,
        feature_size: int,
        batch_size: int,
    ):
        # Generate Pseudo Data: 
        # X in shape of [num_stocks, time_steps, feature_size]
        # Y in shape of [num_stocks, time_steps]
        X = None
        Y = None

    # OverLoad some neccessary function There:

# ==================== Model Definiation ====================
class MyModel():
    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        output_size: int,
    ):
        self.fc = nn.Linear(in_features=input_size, out_features=output_size, bias=True)
        self.act = nn.ReLU()

    # OverLoad some neccessary function There:

# ==================== Training Pipeline ====================

dataset = None
optimizer = None # Define your optimizer
loss = None # Define your loss function
loss_list = [] # Record the training loss
for idx, x, y in enumerate(dataset):
    # Training
    output = MyModel(x)



