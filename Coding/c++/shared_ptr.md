简单的手写 sharedptr实现

~~~c++
#include <iostream>
#include <memory>

template<typename T>
class SharedPtr {
private:
  T* ptr;
  size_t* ref_count;
  
  void release() {
    if (ptr) {
      --(*ref_count);
      if (*ref_count == 0) {
        delete ptr;
        delete ref_count;
      }
    }
  }

public:
  SharedPtr(): ptr(nullptr), ref_count(new size_t(0)) {}
  
  explicit SharedPtr(T* p): ptr(p), ref_count(new size_t(1)) {}
  
  
}

~~~

