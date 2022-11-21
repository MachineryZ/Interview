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
        self.out = self.softmax(self.a2)
        return self.out

    def loss(self, y_hat: np.ndarray, y: np.ndarray) -> np.ndarray:
        # cross entropy loss
        return np.sum(np.log(y_hat) * y)

    def bp(self, x: np.ndarray, y:np.ndarray) -> np.ndarray:
        # See the process in mlp_bp.md

        self.dl_da2 = (-y + self.softmax(self.a2)) # dl/da2
        self.dl_dw2 = self.dl_da2.T @ self.h1 # dl/dw2
        self.dl_dh1 = self.dl_da2 @ self.w2 # dl/dh1
        self.dl_da1 = (self.dl_da2 @ self.w2) * self.partial_sigmoid(self.a1) # dl/da1
        self.dl_dw1 = self.dl_da1.T @ x # dl/dw1

        self.w1 = self.w1 - self.lr * self.dl_dw1
        self.w2 = self.w2 - self.lr * self.dl_dw2

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

    # Step 1 
    # check your forward result:
    out = mymlp.forward(x)
    assert np.linalg.norm(out - np.array([[0.36235674, 0.40728367, 0.23035959]])) < 1e-7

    # Step 2 
    # check your loss
    loss = mymlp.loss(out, y)
    assert np.linalg.norm(loss - -1.015126071106058) < 1e-7

    w1, w2 = mymlp.bp(x, y)
    # Step 2 
    # check your gradients:
    assert np.linalg.norm(mymlp.dl_da2 - np.array([[-0.63764326,  0.40728367,  0.23035959]])) < 1e-7
    assert np.linalg.norm(mymlp.dl_dw2 - np.array([[-0.40732181, -0.47931036, -0.15217421, -0.03860381, -0.09738246, -0.36582423,
        -0.57306758, -0.36619898, -0.53017721, -0.32491802],
        [ 0.2601698,   0.30615125,  0.09719866,  0.02465752,  0.06220137,  0.23366394,
        0.36603706,  0.2339033,   0.33864158,  0.2075358 ],
        [ 0.14715201,  0.17315911,  0.05497555,  0.01394629,  0.03518109,  0.13216029,
        0.20703051,  0.13229568,  0.19153563,  0.11738222]])) < 1e-7
    assert np.linalg.norm(mymlp.dl_dh1 - np.array([[-0.22072836,  0.54220196,  0.2838984,  -0.24103344, -1.74668689, -0.65096623,
        -0.33832413, -0.18948642,  0.76756801,  0.07541716]]))
    assert np.linalg.norm(mymlp.dl_da1 - np.array([[-0.05093011,  0.10120303,  0.05158341, -0.01370905, -0.22601836, -0.15920446,
        -0.03079302, -0.04632553,  0.1075607,   0.0188474 ]]))
    assert np.linalg.norm(mymlp.dl_dw1 - np.array([[ 0.03771251, -0.04810758, -0.05592065, -0.02520829],
        [-0.07493837,  0.09559438,  0.11111971,  0.05009129],
        [-0.03819625,  0.04872466,  0.05663796,  0.02553164],
        [ 0.01015122, -0.0129493,  -0.01505237, -0.00678541],
        [ 0.16736108, -0.21349247, -0.24816545, -0.11186968],
        [ 0.11788702, -0.15038138, -0.17480459, -0.07879958],
        [ 0.02280148, -0.02908648, -0.03381036, -0.01524126],
        [ 0.03430292, -0.04375818, -0.05086487, -0.02292921],
        [-0.07964608,  0.10159971,  0.11810036,  0.05323807],
        [-0.01395604,  0.01780288,  0.02069421,  0.00932868]])) < 1e-7

    # Step 3
    # check your updated weight result
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

    # Bonus Point
    dl_dw2 = mymlp.matrix_differential_propogation(x, y)
    assert np.linalg.norm(dl_dw2 - np.array([[-0.40732181, -0.47931036, -0.15217421, -0.03860381, -0.09738246, -0.36582423,
        -0.57306758, -0.36619898, -0.53017721, -0.32491802],
        [ 0.2601698,   0.30615125,  0.09719866,  0.02465752,  0.06220137,  0.23366394,
        0.36603706,  0.2339033,   0.33864158,  0.2075358 ],
        [ 0.14715201,  0.17315911,  0.05497555,  0.01394629,  0.03518109,  0.13216029,
        0.20703051,  0.13229568,  0.19153563,  0.11738222]])) < 1e-7



