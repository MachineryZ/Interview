template lambda 是 c++17 引入的一个特性，允许在 lambda 表达式中使用模板参数，这使得 lambda 表达式可以更加灵活和通用

相关知识点

- 模板参数，在 lambda 表达式中使用模板参数，使得lambda 可以接受不同类型的参数
- 通用 lambda c++14 引入了通用 lambda 允许在 lambda 表达式中使用 auto 关键词 c++17 进一步拓展了这一特性，允许使用模版参数

常见问题与易错点



~~~c++

#include <iostream>
#include <type_traits>

void demo() {
    // 安全的泛型lambda，仅当类型支持+运算时才执行
    auto safeAdd = [](auto a, auto b) -> decltype(a + b) {
        static_assert(std::is_arithmetic<decltype(a)>::value &&
                      std::is_arithmetic<decltype(b)>::value,
                      "Only arithmetic types are supported");
        return a + b;
    };

    // 正常调用
    std::cout << safeAdd(1, 2) << std::endl; // 输出: 3

    // 尝试错误调用，编译时会失败
    // std::cout << safeAdd("Hello", "World") << std::endl; // 编译错误
}

int main() {
    demo();
    return 0;
}
~~~



- 编写一个template lambda，接受一个容器如 std::vector, std::list 和一个元素，并将该元素添加到容器末尾

~~~C++
#include <iostream>
#include <vector>
#include <list>
int main() {
  auto append = []<typename Container, typename T>(Container& container, T element) {
    container.push_back(element);
  }
  
  std::vector<int> vector = {1, 2, 3};
  append(vec, 4);
  
  std::list<double> lst = {1.1, 2.2, 3.3};
  append(lst, 4.4)
}
~~~



- 编写一个 template lambda，接受一个函数和一个容器，并对容器中的每个元素应用该函数

~~~c++
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  auto apply = []<teypname Func, typename Container>(Func func, Container& container) {
    std::for_each(container.begin(), container.end(), func);
  }
  
  std::vector<int> vector = {1, 2, 3, 4, 5};
  apply([](int& x) { x *= 2}, vec);
  
}
~~~



- 编写一个 template lambda，接受一个函数和一个容器，并返回一个新的容器，其中包含原容器中满足函数条件的元素

~~~C++
#include <iostream>
#include <vector>
#include <algorithm>
int main() {
  auto filter = []<typename Func, typename Container>(Func func, const Container& container) {
    Container result;
    std::copy_if(container.begin(), container.end(), std::back_inserter(result), func);
    return result;
  }
  
  std::vector<int> vec = {1, 2, 3, 4, 5};
  auto filter = filter([](int x) {return x % 2 == 0;}, vec);
  for (int i : filtered)
    std::cout << i << " ";
  std::cout << std::endl;
}
~~~

















































