- 什么是模板部分特化 template partial specialization

模板部分特化 template partial specialization 是 c++ 模板编程中的一个高级特性，允许你为模板参数的某些特定组合提供专门的实现。与模板全特化（template full specialization）不同，部分特化不完全指定所有模板参数而是指定其中的一部分

- 模板部分特化的基本结构

假设你有一个模板类 mytemplate 你可以为某些特定的模板参数组合提供部分特化

~~~C++
template<typename T1, typename T2>
class MyTemplate{
public:
  void print() {
    std::cout << "General template" << std::endl;
  }
};

template <typename T2>
class MyTemplate<int, T2> {
public:
  void print() {
    std::cout << "Partial specialization for T1 = int" << std::endl;
  }
};

~~~

- 模板部分特化和模板全特化有什么区别

全特化：完全指定所有模板参数，为特定的模板参数组合提供专门的实现

部分特化：只指定部分模板参数，为某些特定的模板参数组合提供专门的实现



- 模板部分特化在什么情况下有用

优化性能：为某些特定的类型提供专门的逻辑或行为

处理特定类型：为某些特定的类型提供专门的逻辑或行为

代码复用：通过部分特化减少代码重复，提高代码的可维护性



- 实现一个模板类 MyContainer 并为 std::vector 提供部分特化

~~~c++
#include <iostream>
#include <vector>
template<typename T>
class MyContainer {
public:
  void print() {
    std::cout << "General container" << std::endl;
  }
};

template <typename T>
class MyContainer<std::vector<T>> {
public:
  void print() {
    std::print << "Partial specialization for std::vector" << std::endl;
  }
};



~~~









































