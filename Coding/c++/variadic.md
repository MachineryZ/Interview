Variadic Functions

可变参数函数 variadic function 是一种函数，它能够接受可变数量的参数。

1. 参数数量不确定
2. 参数类型不确定
3. 使用标准库，通常使用标准库中的 stdarg.h



示例写一个简单的可变参数函数，用于计算一组整数的和

~~~C++
int sum(int count, ...) {
  int total = 0;
  va_list args;
  
  va_start(args, count);
  
  for (int i = 0; i < count; ++i) {
    int value = va_arg(args, int);
    total += value;
  }
  
  va_end(args);
  return total;
}

int main() {
  int result = sum(3, 1, 2, 3);
  return 0;
}

~~~

-------

可变参数模板函数

c++11引入的一个重要特性，允许你定义接受任意数量和任意类型参数的模板函数或类。可变参数模板提供了类型安全的可变参数处理方式，避免了传统可变参数函数的类型安全问题

~~~C++
#include <iostream>

template <typename T>
T sum(T value) {
  return value;
}

template <typename T, typename... Args>
T sum(T first, Args... args) {
  return first + sum(args...);
}

int main() {
  int result = sum(1, 2, 3, 4, 5);
  double result2 = sum(1.1, 2.2, 3.3);
  return 0;
}

~~~

可变参数模板类

~~~c++
#include <iostream>
#include <tuple>

template <typename... Args>
class MyTuple {
public:
	MyTuple(Args... args) : data(args...) {}
  
  void print() {
    print_tuple(data, std::index_sequence_for<Args...>{});
  }
private:
  std::tuple<Args...> data;
  template <std::size_t... Is>
  void print_tuple(const std::tuple<Args...>& t, std::index_sequence<Is...>) {
    ((std::cout << std::get<Is>(t) << " "), ...);
    std::cout << std::endl;
  }
};

int main() {
  MyTuple<int, double, std::string> 4(42, 3.14, "Hello")
    t.print()
}
~~~





































