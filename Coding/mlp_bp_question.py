# For this coding problem, we are about to simulate a deep learning 
# training process. 
# In computer vision field, classification is a very important
# and traditional field. Assume that we have a some pseudo data input 
# for a mlp (multi-layer perceptron) model.

# Q1: How should we arrange the sequence of fully-connected layer, activation
# layer, batch normalization layer? Why?
# x - relu - fc - bn
# x - relu - bn - fc
# x - bn - fc - relu
# x - bn - relu - fc
# x - fc - relu - bn
# x - fc - bn - relu

# Q2: What is the role for batch normalization playing for?

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
        x = np.random.randn(self.batch_size, self.input_size) # [bs, input_size]
        y = np.random.randint(0, self.num_classes, (self.batch_size, )) # [bs,]
        y = np.eye(self.num_classes)[y] # [bs, num_cls]
        return x, y

    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        # y = sigmoid(x)
        return None
    
    def partial_sigmoid(self, x: np.ndarray) -> np.ndarray:
        # y' = d(sigmoid(x))/d(x)
        return None

    def softmax(self, x: np.ndarray) -> np.ndarray:
        # x = [batch_size, dim] -> do softmax in column-wise dimension
        return None

    def forward(self, x: np.ndarray) -> np.ndarray:
        # Two layer mlp
        # x -> fc -> sigmoid -> fc -> softmax
        # Notice that we use the formulation y = x W.T (without bias)  
        self.a1 = None# fc1 output 
        self.h1 = None# sigmoid output 
        self.a2 = None# fc2 output 
        self.out = None# softmax output
        return None
    
    def loss(self, y_hat: np.ndarray, y: np.ndarray) -> np.ndarray:
        # yhat
        # cross entropy loss
        return None

    def bp(self, x: np.ndarray, y:np.ndarray) -> np.ndarray:
        # Update w1 and w2
        self.dl_da2 = None # partial loss to partial a2
        self.dl_dw2 = None# partial loss to partial w2
        self.dl_dh1 = None# partial loss to partial h1
        self.dl_da1 = None# partial loss to partial a1
        self.d1_dw1 = None# partial loss to partial w1

        # SGD Update w1 and w2:
        self.w1 = None
        self.w2 = None
        return self.w1, self.w2

    def matrix_differential_propogation(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        # Bonus
        # Matrix-Matrix function derivatives
        # Double check for gradient
        return None


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
    assert np.linalg.norm(loss - np.array([[-1.01512607, -0. ,        -0.,        ]])) < 1e-7

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

    dl_dw2 = mymlp.matrix_differential_propogation(x, y)
    assert np.linalg.norm(dl_dw2 - np.array([[-0.40732181, -0.47931036, -0.15217421, -0.03860381, -0.09738246, -0.36582423,
        -0.57306758, -0.36619898, -0.53017721, -0.32491802],
        [ 0.2601698,   0.30615125,  0.09719866,  0.02465752,  0.06220137,  0.23366394,
        0.36603706,  0.2339033,   0.33864158,  0.2075358 ],
        [ 0.14715201,  0.17315911,  0.05497555,  0.01394629,  0.03518109,  0.13216029,
        0.20703051,  0.13229568,  0.19153563,  0.11738222]])) < 1e-7
