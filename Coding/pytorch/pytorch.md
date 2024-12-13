PyTorch框架是一个基于动态计算图机制的机器学习框架，以Python优先，具有很强的易用性和灵活性，方便用户编写和调试网络代码。为了保存和加载网络模型，PyTorch框架提供了TorchScript方法，用于创建可序列化和可优化模型。TorchScript IR作为PyTorch模型的中间表示，通过JIT即时编译的形式，将Python代码转换成目标模型文件。任何TorchScript程序都可以在Python进程中保存，并加载到没有Python依赖的进程中。



PyTorch框架采用命令式编程方式，其TorchScript IR以基于SSA的线性IR为基本组成形式，并通过JIT即时编译的Tracing和Scripting两种方法将Python代码转换成TorchScript IR。如下Python代码使用了Scripting方法并打印其对应的中间表示图：

~~~python
import torch

@torch.jit.script
def test_func(input):
    rv = 10.0
    for i in range(5):
        rv = rv + input
        rv = rv/2
    return rv

print(test_func.graph)

~~~



~~~python
graph(%input.1 : Tensor):
  %9 : int = prim::Constant[value=1]()
  %5 : bool
~~~



































