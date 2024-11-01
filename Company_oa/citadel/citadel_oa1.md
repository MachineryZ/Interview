In Python, which of the following gives the correct order, from first to last, of scope resolution

1. Local function, enclosing function, global statements, built-in names
2. local function, global statements, built-in names, enclosing function
3. built-in names, global statements, local function, enclosing function
4. built-in names, global statements, enclosing function, local function
5. local function, global statements, enclosing function, built-in names

正确答案 1，变量的作用域解析遵循 LEGB 规则，这表示查找变量的时候，python会按照一下顺序进行：局部 local 作用域，封闭 enclosed 作用域，全局 global 作用域 和 内置 built-in 作用域

---

In Python, if you had to iteratively read over two files line-by-line, which of the following would be the best way to accomplish this task?

1. Use with open () to open the two file as f1 and f2 then use readline() and a for loop to iteratively read lines from each files
2. Use open() to open the two file as f1 and f2, then use readline() and a for loop to iteratively read lines from each file
3. Use with open() to open the two files as f1 and f2, then use zip() to iterate over the two files together
4. Use open() to open the two files  as f1 and f2, then use zip() to iterate over the two files together
5. Implement a file seek () function and call the function for the two files simultaneously

正确答案 3 

The best way to iteratively read over two files line-by-line in Python is:

**C. Use `with open ()` to open the two files as `f1` and `f2`, then use `zip()` to iterate over the two files together.**

### Explanation:

- **`with open()`**: This ensures that the files are properly closed after the block of code is executed, even if an exception occurs. This is a best practice for file handling in Python.
- **`zip()`**: This function allows you to iterate over multiple iterables (like file objects) simultaneously, making it easy to read lines from both files in parallel.

### Why not the others?

- **A and B**: Using `readline()` and a `for` loop is not the most Pythonic way to read files line-by-line. It’s more common to use `for line in file` or `zip()` for this purpose.
- **D**: While `zip()` is a good approach, using `open()` without `with` is not recommended because it doesn’t ensure that the files are closed properly.
- **E**: Implementing a `seek()` function and calling it for the two files simultaneously is unnecessary and overly complex for this task.

So, option **C** is the best choice for iteratively reading two files line-by-line in Python.

---

In Python, which of the following statements are true?:

• I. The pipe module can be used to run shell commands in a program • Il. A pickle can store any Python object except tuples in string format • Ill. If you have a Python program called player.py, then you can import the module by running import player. py 

A. l and Il only

B. I and Ill only

C. Il and Ill only

D. I, Il, and Ill

E. None of A through D

The correct answer is:

**E. None of A through D**

### Explanation:

- **I. The pipe module can be used to run shell commands in a program**:
  - **False**: The correct module to run shell commands in Python is `subprocess`, not `pipe`. The `pipe` module is not a standard Python module for running shell commands.
- **II. A pickle can store any Python object except tuples in string format**:
  - **False**: The `pickle` module can store any Python object, including tuples, in a serialized format. It does not store objects in string format directly; it serializes them into a binary format.
- **III. If you have a Python program called player.py, then you can import the module by running import player.py**:
  - **False**: The correct way to import a module named `player.py` is `import player`, not `import player.py`. The `.py` extension is not included in the import statement.

Since none of the statements are true, the correct answer is **E. None of A through D**.

---

Suppose you are given a highway congestion dataset with one feature - the average vehicle speed. It is found that if the average speed is above 70 kilometers per hour, then there are no accidents on the highway. However, if the average speed is below 70 kilometers per hour, then there is at least one accident on the highway. You would like to build a classifier for this problem using support vector machines (SVM). Your colleague suggests that this approach could be problematic due to imbalances in the distribution of vehicle speeds. Is your colleague correct, and why or why not?

A. Your colleague is correct - a SVM's performance will suffer because of the reason he mentioned

B. Your colleague is incorrect - SVMs assign greater weights to the data near the boundary so will perform fine

C. Your colleague is correct - SVMs are bad at classifying traffic-related data in general

D. Your colleague is incorrect - although linear VMs will perform poorly, radial basis VMs will perform fine

E. None of the above

**A. Your colleague is correct - a SVM's performance will suffer because of the reason he mentioned**

### Explanation:

- **Imbalanced Data**: In this scenario, the dataset is imbalanced because most of the time, the average vehicle speed is above 70 km/h (no accidents), and only rarely is it below 70 km/h (accidents). This imbalance can lead to poor performance in classification tasks, especially for minority classes (in this case, the class representing accidents).
- **SVM Performance**: Support Vector Machines (SVMs) are sensitive to class imbalance. When the classes are imbalanced, the SVM might be biased towards the majority class (no accidents), leading to poor classification performance for the minority class (accidents). This is because the SVM tries to maximize the margin between the classes, and with an imbalanced dataset, it might focus more on correctly classifying the majority class, ignoring the minority class.
- **Weight Adjustment**: While it is true that SVMs can assign greater weights to data near the boundary, this alone does not address the issue of class imbalance. Techniques such as oversampling the minority class, undersampling the majority class, or using class weights can help mitigate the impact of class imbalance, but the default behavior of SVMs without these adjustments will still suffer.

Therefore, your colleague is correct in suggesting that the performance of the SVM classifier could be problematic due to the imbalanced distribution of vehicle speeds.

---

**Bayesian**

3% of a country's population has a particular disease. The national health institute has developed a test for this disease: the test has a 98% "true positive" rate (the probability that a person will test positive given that they have the disease). However, it also has a 4% "false positive" rate (the probability that a person will test positive given that they do NOT have the disease). If you simultaneously take the test twice, and it comes out with two positive results, which of the following is CLOSEST to the probability that you actually have the disease, assuming the tests are independent?

A. 0.96

B. 0.95

C. 0.94

D. 0.93

E. 0.92

假设患病事件是 D

P(D) = 0.03

P(~D) = 0.97

假设测试阳性事件是 + 

P(+|D) = 0.98

P(+|~D) = 0.04

患病并且两次测试都为阳性

P(D++) = P(D) * P(+|D) * P(+|D) = 0.03 * 0.98 * 0.98 =0.02881

不患病并且两次测试都为阳性

P(~D++) = P(~D)  * P(+|~D) * P(+|~D) = 0.97 * 0.04 * 0.04 =  0.001552

两次都测试阳性的情况下，患病的概率

P(D|++) = P(D++)/P(++)

P(++) = 0.028812 + 0.001552 = 0.030364

P(D|++) = 0.02881/0.030364 = 0.94887所以选C

-----

What is the MAIN advantage of using a random forest over a decision tree?

A. It can be parallelized

B. It captures non-linear decision boundaries

C. It allows for batch learning

D. It reduces overfitting

E. It uses less memory

### 解释：

随机森林（Random Forest）是一种集成学习方法，它通过构建多个决策树并将它们的预测结果进行组合来提高模型的性能。随机森林的主要优势之一是它能够减少过拟合（overfitting）。

#### 为什么随机森林能减少过拟合？

1. **Bagging（Bootstrap Aggregating）**: 随机森林通过使用自助采样（bootstrap sampling）从训练数据中随机抽取多个子集，每个子集用于训练一个决策树。这使得每棵树都是在不同的数据子集上训练的，从而减少了模型对特定数据的依赖性。
2. **Feature Randomness**: 在构建每棵树时，随机森林还会随机选择特征子集进行分裂，而不是使用所有特征。这种特征随机性进一步增加了树之间的多样性，减少了过拟合的风险。
3. **Ensemble Effect**: 由于随机森林是由多棵树组成的，最终的预测结果是通过对所有树的预测结果进行平均（回归问题）或投票（分类问题）得到的。这种集成效应使得模型更加稳定和泛化能力更强。

### 其他选项的解释：

- **A. It can be parallelized**: 虽然随机森林可以并行化处理，但这并不是其主要优势。决策树也可以通过并行化来加速训练。
- **B. It captures non-linear decision boundaries**: 随机森林和决策树都能捕捉非线性决策边界，但这并不是随机森林的主要优势。
- **C. It allows for batch learning**: 随机森林和决策树都可以进行批量学习，但这并不是随机森林的主要优势。
- **E. It uses less memory**: 随机森林通常比单棵决策树使用更多的内存，因为它需要存储多棵树的信息。

因此，随机森林的主要优势是减少过拟合，选项 D 是正确答案。

----

Which of the following machine learning algorithms is NOT sensitive to the initial variables used in the optimization algorithm?

A. Hidden Markov models

B. Artificial neural networks

C. Random forests

D. Support vector machines

E. k - nearest neighbors

随机森林（Random Forests）是一种集成学习方法，它通过构建多个决策树并将它们的预测结果进行组合来提高模型的性能。随机森林的一个主要特点是它对初始变量的选择不敏感。

#### 为什么随机森林对初始变量不敏感？

1. **Bagging（Bootstrap Aggregating）**: 随机森林通过使用自助采样（bootstrap sampling）从训练数据中随机抽取多个子集，每个子集用于训练一个决策树。这种随机性使得每棵树都是在不同的数据子集上训练的，从而减少了模型对特定数据的依赖性。
2. **Feature Randomness**: 在构建每棵树时，随机森林还会随机选择特征子集进行分裂，而不是使用所有特征。这种特征随机性进一步增加了树之间的多样性，减少了模型对初始变量的敏感性。
3. **Ensemble Effect**: 由于随机森林是由多棵树组成的，最终的预测结果是通过对所有树的预测结果进行平均（回归问题）或投票（分类问题）得到的。这种集成效应使得模型更加稳定和泛化能力更强，从而减少了对初始变量的敏感性。

### 其他选项的解释：

- **A. Hidden Markov models**: 隐马尔可夫模型（HMM）对初始变量的选择是敏感的，因为它们依赖于初始状态概率和转移概率矩阵。
- **B. Artificial neural networks**: 人工神经网络（ANN）对初始权重的选择非常敏感，因为它们依赖于梯度下降等优化算法，初始权重的选择会影响训练过程和最终模型的性能。
- **D. Support vector machines**: 支持向量机（SVM）对初始变量的选择是敏感的，因为它们依赖于核函数的选择和超参数的设置。
- **E. k - nearest neighbors**: k近邻算法（k-NN）对初始变量的选择是敏感的，因为它们依赖于距离度量的选择和k值的设置。

因此，随机森林是对初始变量选择不敏感的机器学习算法，选项 C 是正确答案。

----

You have two fair coins and one coin with heads on both sides. You pick a coin at random and toss it twice. If it reads heads both times, what is the probability it also reads heads after a third toss?

A. 1/6

B. 1/3

C. 1/2

D. 2/3

E. 5/6

假设事件 F 是选到了 fair 硬币

P(F) = 2/3

P(~F) = 1/3

P(2+|F) = 1/4

P(2+|~F) = 1

P(2+, F) = 1/4 * 2/3 = 1/6

P(2+, ~F) = 1 * 1/3 = 1/3

P(2+) = 1/6 + 1/3 = 1/2 

那么在已知2次都是正面的情况下

P(F|2+) = P(2+, F)/P(2+) = 1/6 / 1/2 = 1/3

P(~F|2+) = P(2+, ~F) / P(2+) = 1/3 / 1/2 = 2/3

P(+) * P(F|2+) + P(+) * P(~F|2+) = 1/3 * 1/2 + 2/3 = 5/6

---













































