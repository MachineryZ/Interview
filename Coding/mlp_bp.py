# For this coding problem, we are about to simulate a deep learning 
# training process. 
# In computer vision field, classification problem is a very important
# and traditional problem. Assume that we have a some pseudo data input 
# for a mlp (multi-layer perceptron) model.

# Q1: How should we arrange the sequence of fully-connected layer, activation
# layer, batch normalization layer? Why?
# x - relu - fc - bn 
# x - relu - bn - fc 
# x - bn - fc - relu 
# x - bn - relu - fc 
# x - fc - relu - bn
# x - fc - bn - relu

# Q2: What is the role for batch normalization plays for?

# Q3: Assume we need to define a 2-layer mlp. 
# We have our pseudo data  x in shape of [batch_size, input_size]
# We have our pseudo label y in shape of [batch_size, num_classes](one-hot vector)
# We need you to !!!only!!! use numpy to build a training pipeline, 
# 1. Use Sigmoid as your activation function
# 2. Use cross entropy loss
# 3. No batch normalization
# 4. Write your own back propogation progess to update your weights of fc layers.
# 5. Using SGD optimizer algorithm
# 6. Don't forget to do softmax in final output
# 7. Finish the api we given to you

import numpy as np

# ============================== Question ==============================
class MyMLP():
    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        num_classes: int,
        lr: float,
        batch_size: int = 1,
    ):
        self.input_size = input_size
        self.num_classes = num_classes
        self.batch_size = batch_size
        self.lr = lr

        self.w1 = np.random.randn(hidden_size, input_size)
        self.w2 = np.random.randn(num_classes, hidden_size)

    def generate_data(self):
        x = np.random.randn(self.batch_size, self.input_size)
        y = np.random.randint(0, self.num_classes, (self.batch_size, ))
        y = np.eye(self.num_classes)[y]
        return x, y

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        # y = sigmoid(x)
        return 
    
    def partial_sigmoid(self, x: np.ndarray) -> np.ndarray:
        # y' = d(sigmoid(x))/d(x)
        return 

    def softmax(self, x: np.ndarray) -> np.ndarray:
        # x = [batch_size, dim] -> do softmax in column-wise dimension
        return

    def forward(self, x: np.ndarray) -> np.ndarray:
        # Two layer mlp
        # x -> fc -> sigmoid -> fc -> softmax
        # Notice that we use the (x W + b ) kind of fc  
        return 

    def bp(self, x: np.ndarray, y:np.ndarray) -> np.ndarray:
        # Update w1 and w2
        return

if __name__ == '__main__':
    np.random.seed(2022)
    mymlp = MyMLP(input_size=4, hidden_size=10, num_classes=3, lr=0.01, batch_size=1)
    x, y = mymlp.generate_data()
    out = mymlp.forward(x)
    w1, w2 = mymlp.bp(x, y)
    assert np.linalg.norm(w1 - np.array([[-0.00090502, -0.27442035, -0.13872636,  1.98493824],
            [ 0.28285871,  0.75985271,  0.29987041,  0.53979636],
            [ 0.37387925,  0.37732615, -0.09077957, -2.30619859],
            [ 1.14265851, -1.53552479, -0.86360149,  1.01661279],
            [ 1.03229027, -0.8223573,   0.02138651, -0.38222486],
            [-0.30536435,  0.99879532, -0.12552579, -1.47509791],
            [-1.94113434,  0.83393979, -0.56687978,  1.17463937],
            [ 0.3187258,   0.19130801,  0.36977883, -0.10091857],
            [-0.94101303, -1.40515771,  2.07946601, -0.12084862],
            [ 0.75993144,  1.82725411, -0.66093403, -0.80789955]])) < 1e-7
    assert np.linalg.norm(w2 - np.array([[ 0.89187333, -0.21265435, -0.93800277,  0.59992435,  2.22408652,  1.0036637,
        1.15540522, -0.1519143,  -1.64527408, -1.45186499],
        [ 0.31815989,  0.80828812, -0.24177658,  0.16487451, -0.03412259,  0.08552794,
        1.03048616, -1.06316559, -1.01697087, -0.42230754],
        [ 0.93068173,  0.31559234, -0.943021,    0.32112784, -1.36990554, -0.21448964,
        -0.11681657,  0.62104636,  0.55332894, -2.95860606]])) < 1e-7

# ============================== Answer ==============================

import numpy as np
from typing import List
class MyMLP():
    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        num_classes: int,
        lr: float,
        batch_size: int = 1,
    ):
        self.input_size = input_size
        self.num_classes = num_classes
        self.batch_size = batch_size
        self.lr = lr

        self.w1 = np.random.randn(hidden_size, input_size)
        self.w2 = np.random.randn(num_classes, hidden_size)

    def generate_data(self):
        # Genereate Pseudo data 
        # Randn for x
        # Randint one-hot for y
        x = np.random.randn(self.batch_size, self.input_size)
        y = np.random.randint(0, self.num_classes, (self.batch_size, ))
        y = np.eye(self.num_classes)[y]
        return x, y

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        # Sigmoid Activation
        return 1 / (1 + np.exp(-x))
    
    def partial_sigmoid(self, x: np.ndarray) -> np.ndarray:
        # Derivatives of sigmoid activation
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def softmax(self, x: np.ndarray) -> np.ndarray:
        # Softmax Layer
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

    def forward(self, x: np.ndarray) -> np.ndarray:
        # Feed Forward for mlp
        self.a1 = x @ self.w1.T
        self.h1 = self.sigmoid(self.a1)
        self.a2 = self.h1 @ self.w2.T
        out = self.softmax(self.a2)
        return out

    def bp(self, x: np.ndarray, y:np.ndarray) -> np.ndarray:
        # See the process in mlp_bp.md

        dl_da2 = (-y + self.softmax(self.a2)) # dl/da2
        dl_dw2 = dl_da2.T @ self.h1 # dl/dw2
        dl_dh1 = dl_da2 @ self.w2 # dl/dh1
        dl_da1 = (dl_da2 @ self.w2) * self.partial_sigmoid(self.a1) # dl/da1
        dl_dw1 = dl_da1.T @ x # dl/dw1

        self.w1 = self.w1 - self.lr * dl_dw1
        self.w2 = self.w2 - self.lr * dl_dw2
        return self.w1, self.w2
        
    def matrix_differential_propogation(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        # Matrix-Matrix function derivatives
        # Double check for gradient
        dl_dw2 = -np.kron(self.h1, y.T) + np.kron(self.h1, np.exp(self.a2).T) / np.sum(np.exp(self.a2))
        return dl_dw2

if __name__ == '__main__':
    np.random.seed(2022)
    mymlp = MyMLP(input_size=4, hidden_size=10, num_classes=3, lr=0.01, batch_size=1)
    x, y = mymlp.generate_data()
    out = mymlp.forward(x)
    w1, w2 = mymlp.bp(x, y)
    assert np.linalg.norm(w1 - np.array([[-0.00090502, -0.27442035, -0.13872636,  1.98493824],
            [ 0.28285871,  0.75985271,  0.29987041,  0.53979636],
            [ 0.37387925,  0.37732615, -0.09077957, -2.30619859],
            [ 1.14265851, -1.53552479, -0.86360149,  1.01661279],
            [ 1.03229027, -0.8223573,   0.02138651, -0.38222486],
            [-0.30536435,  0.99879532, -0.12552579, -1.47509791],
            [-1.94113434,  0.83393979, -0.56687978,  1.17463937],
            [ 0.3187258,   0.19130801,  0.36977883, -0.10091857],
            [-0.94101303, -1.40515771,  2.07946601, -0.12084862],
            [ 0.75993144,  1.82725411, -0.66093403, -0.80789955]])) < 1e-7
    assert np.linalg.norm(w2 - np.array([[ 0.89187333, -0.21265435, -0.93800277,  0.59992435,  2.22408652,  1.0036637,
        1.15540522, -0.1519143,  -1.64527408, -1.45186499],
        [ 0.31815989,  0.80828812, -0.24177658,  0.16487451, -0.03412259,  0.08552794,
        1.03048616, -1.06316559, -1.01697087, -0.42230754],
        [ 0.93068173,  0.31559234, -0.943021,    0.32112784, -1.36990554, -0.21448964,
        -0.11681657,  0.62104636,  0.55332894, -2.95860606]])) < 1e-7
    
