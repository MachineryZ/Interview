什么是 crtp

crtp curiously recurring template pattern是一种c++设计模式，其中派生类作为模板参数传递给基类。这种模式允许基类在编译时知道派生类的类型，从而实现静态多态性。crtp 通常用于优化代码，减少虚函数调用的开销，并提供编译时多态性



关键点

- 基类模板：基类是一个模板类，接受派生类作为模板参数
- 派生类继承基类；派生类继承基类，并将自身类型作为模板参数传递给基类
- 静态多态性：通过模板参数，基类可以在编译时知道派生类的类型，从而实现静态多态性

~~~C++
template <typename Derived>
class Base{
public:
  void interface() {
    static_cast<Derived*>(this)->implementation();
  }
};

class Derived : public Base<Derived> {
public:
  void implementation() {
    std::cout << "Derived implementation" << std::endl;
  }
};

int main

~~~



- crtp 的主要优点是什么？

crtp的主要优点包括

1. 静态多态性 通过模板实现多态，避免了虚函数调用的开销
2. 基类可以复用派生类的实现，减少代码重复
3. 类型安全，由于使用模板，编译器可以在编译时进行类型检查，避免运行时的错误



- crtp 和虚函数有什么区别

crtp和虚函数的主要区别在于

1. 性能 crtp 通过模板实现静态多态，避免了虚函数调用的开销，性能更高
2. 灵活性，虚函数可以在运行时动态绑定，而 crtp 在编译时确定类型
3. 代码结构，crtp 需要派生类显式继承基类模板，而虚函数通过继承和重写实现多态



- 实现一个简单的crtp基类，使得派生类可以调用基类的print 方法，并输出派生类的类型名称

~~~C++
#include <iostream>
#include <typeinfo>

template<typename Derived>
class Base {
public:
  void print() const {
    std::cout << "Type" << typeid(Derived).name() << std::endl;
  } 
};

class Derived1 : public Base<Derived1> {
  // 1
};

class Derived2 : public Base<Derived2> {
  
};

int main() {
  Derived d1;
  Derived d2;
  
  d1.print();
  d2.print();
  
  return 0;
}
~~~



- 使用 crtp 实现一个简单的单例模式

~~~c++
#include <iostream>
#include <mutex>

template<typename Derived>
class Singleton {
public:
  static Derived& getInstance() {
    static Derived instance;
    return instance;
  }
protected:
  Singleton() = default;
  ~Singleton() = default;

private:
  Singleton(const Singleton&) = delete;
  Singleton& operator=(const Singleton&) = delete;
};

class MySingleton : public Singleton<MySingleton> {
public:
  void doSomething() {
    std::cout << "Doing something..." << std::endl;
  }
};

int main() {
  MySingleton& instance = MySingleton::getInstance();
  instance.doSomething();
  return 0;
}


~~~































