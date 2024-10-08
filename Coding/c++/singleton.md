单例

设计模式的话题一直是一个重点，从分类、线程安全来讲述单例

一般来说，熟知的单例模式是下面这样的

~~~c++
class singleton {
private:
  singleton() {}
  static singleton *p;
public:
  static singleton *instance();
};

singleton *singleton::p = nullptr;
singleton* singleton::instance() {
  if (p == nullptr)
    p = new singleton();
  return p;
}
~~~

这是一个非常简单的实现，将构造函数声明为 private 或 protect 防止被外部函数实例化，内部有一个静态的类指针保存唯一的实例，实例的实现由一个 public 方法来实现，该方法返回该类的唯一实例。

当然这个代码只适合在单线程下，当多线程时，是不安全的。考虑两个线程同时调用 instance 方法且同时检测到