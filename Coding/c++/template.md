template 中 typename 和 class 的区别：
在 c++ 中 typename 和 class 关键字都用在模版编程和泛型编程中引入类型参数。他们在语法上有一些差异，但在大多数情况下可以互换使用。
以下是他们之间的区别和使用场景：
1. 类型参数的位置：使用 typename 关键字时，类型参数可以出现在模版参数列表中的任何位置。而class 关键字时，类型参数通常出现在模版参数列表的开头
~~~c++
template <typename T, int N>
class MyClass1 {};

template <class T, int T>
class MyClass2 {};
~~~