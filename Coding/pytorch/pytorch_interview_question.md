PyTorch Question

---

register_buffer 是什么

register_buffer 是 pytorch 中的一个方法，用于将一个张量或缓冲区注册为模型的非训练参数。它将张量或缓冲区添加到模型的缓冲区列表中，这意味着会被模型跟踪，但不会被当作模型的可训练参数。register buffer 方法如下：

~~~python
register_buffer(name: str, tensor: torch.Tensor, persistent: bool = True) -> None
~~~

参数说明：

- name 缓冲区名称，用于在模型中唯一标识缓冲区
- tensor 要注册的张量或缓冲区
- persistent 一个 bool 值，指示缓冲区是否应该被保存在模型的状态字典中

使用 register_buffer 方法可以方便的将一些需要在模型中持久存在的状态（如移动平均值，标准化参数等）注册为缓冲区。这样，在保存和加载模型时，这些缓冲区的值也会被保存和加载，而不会被当作模型的可训练参数（被视为模型的常量，如果需要在训练过程中更新缓冲区的值，可以使用其他方法或手动计算并更新缓冲区的值）

以下一个示例演示如何使用 register_buffer 方法注册一个缓冲区

~~~python
import torch
import torch.nn as nn

class MyModel(nn.Module):
  def __init__(self):
    super(MyModel, self).__init__()
    self.register_buffer("running_mean", torch.zeros(1))
    self.register_buffer("running_var", torch.zeros(1))
    
  def forward(self, x):
    x = (x - running_mean) / torch.sqrt(self.running_var)
    return x 
~~~



























