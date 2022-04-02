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
"""
import torch
import numpy as np

# ==================== Data generation ====================

# ==================== Model Definiation ====================

# ==================== Training Pipeline ====================


