简历问题





-----

智能指针和 stl 库

std::unique_ptr

- 独占所有权：每个 std::unique_ptr 实例独占它所管理的对象，不能复制，只能转移所有权。

- 轻量级：由于不需要维护引用计数，性能开销较小。

- 内存管理：在对象生命周期结束时自动释放内存，确保不会发生内存泄漏。

- 用途：适用于确保单一所有权的场景，如动态分配资源的函数内部，或者需要明确控制对象生命周期的情况下

std::shared_ptr

- 共享所有权：允许多个智能指针共享同一个对象，每个指针都持有该对象的引用计数。

- 引用计数：每当一个新的 std::shared_ptr 指向相同的对象时，引用计数增加；当一个 std::shared_ptr 被销毁或重置时，引用计数减少。引用计数为零时，销毁对象。

- 灵活性：适用于需要共享资源的场景，如共享数据结构或跨多个函数/对象的资源管理。

- 线程安全：引用计数的修改是线程安全的，但对象本身的访问需要额外的同步。

std::weak_ptr

- 非拥有型指针：不管理对象的生命周期，只是观察对象是否还存在。

- 避免循环引用：常与 std::shared_ptr 一起使用，防止循环引用导致的内存泄漏。

- 获取共享对象：通过调用 lock() 方法尝试获取一个 std::shared_ptr，如果对象仍然存在则成功，否则返回空指针。

- 用途：适用于缓存机制、观察者模式等需要弱引用的场景，确保引用的对象可以被垃圾回收。

std::auto_ptr

- 过时的智能指针：在 C++11 中被 std::unique_ptr 替代。

- 独占所有权：类似于 std::unique_ptr，但语义不同，容易导致意外错误（如隐式复制导致所有权转移）。

- 已弃用：在现代 C++ 编程中应避免使用，推荐使用 std::unique_ptr 替代。

c++ 中的智能指针

智能指针主要用于管理在堆上分配的内存，它将普通的指针封装为一个栈对象。当栈对象的生命周期结束后，会在析构函数中释放掉申请的内存，从而防止内存泄漏。c++ 11 中最常用的智能指针类型为 shared_ptr，它采用引用计数的方法，记录当前内存资源被多少个智能指针引用。该引用计数的内存在堆上分配，当新增一个引用计数时 +1，当过期时引用计数时 -1；只有引用计数为0时，智能指针才会自动释放引用的内存资源。对 shared_ptr 进行初始化时不能将一个普通指针直接赋值给智能指针，因为一个时指针，一个时类。可以通过 ma ke_shared 函数或者通过构造函数传入普通指针。并可以通过 get 函数获得普通指针。

智能指针有没有内存泄漏的情况？当两个对象互相使用一个 shared_ptr 成员变量指向对方，会造成循环引用，使引用计数失效，从而导致内存泄漏。例如

~~~c++
class Parent {
private:
	std::shared_ptr<Child> ChildPtr;
public:
	void setChild(std::shared_ptr<child> child) {
		this-ChildPtr = child;
	}
  void doSomething() {
    if (this->ChildPtr.use_count()) {}
  }
  ~Parent(){}
};
~~~

~~~c++
class Child {
private:
  std::shared_ptr<Parent> ParentPtr;
public:
  void setParent(std::shared_ptr<Parent> parent) {
    this->ParentPtr = parent;
  }
  void doSomething() {
    if (this->ParentPtr.use_count()) {}
  }
  ~Child() {}
};
~~~



- 智能指针的内存泄漏如何解决？

为了解决循环引用导致的内存泄漏，引入了 weak_ptr 弱指针，weak_ptr的构造函数不会修改引用计数的值，从而不会对对象的内存进行管理，其类似一个普通指针，但不指向引用计数的共享内存，但是弱指针可以检测到所管理的对象是否已经被释放，从而避免非法访问。

- 有什么智能指针做不到而普通指针能做到？

**原始内存操作**：普通指针可以直接指向任何内存地址，无论是动态分配内存、栈上的内存还是全局内存。而智能指针一般只能管理动态分配的内存，不能直接向栈上的内存或全局内存。

**灵活性和控制性**：普通指针允许程序员对内存管理有更多的控制权，比如手动分配和释放内存。智能指针在某种程度上限制了这种控制，以避免内存泄漏和悬空指针的问题。

**非标准内存管理**：对于一些自定义的内存分配策略或特殊的内存管理需求（如内存池），普通指针可能更适合，智能指针的内存管理方式是固定的，不适合这种场景

**对象生命周期的精确控制**：在某些高性能或实时系统中，开发者可能需要精确控制对象的生命周期。普通指针允许开发者决定对象的确切析构时间，而智能指针则是在其生命周期结束时自动销毁对象

**无开销场景**：在某些性能关键的应用中，智能指针带来的额外开销（如引用计数的维护）可能是不必要的。普通指针在这种情况下没有这些额外的开销。

~~~c++
void compute(int* data, size_t size) {
  for (size_t i = 0; i < size; ++i) {
    data[i] = i*i;
  }
}
~~~

指针算数和数组操作：普通指针可以进行指针算数操作（如指针加减），并且可以直接用来遍历数组。而智能指针通常不支持这些操作，虽然可以通过迭代器实现类似功能，但使用上不如普通指针直接。

- shared_ptr 是线程安全的么？

引用计数的增减是线程安全的，但对象本身的操作需要额外的同步

- 智能指针可以复制吗？

shared_ptr 可以复制、增加引用计数，unique_ptr 不行；

- 什么时候应该使用 shared_ptr 和 weak_ptr 混合使用？

当需要一个指针观察但不拥有对象时，使用 weak_ptr，例如，缓存机制可以用 weak_ptr 避免缓存对象不被释放

~~~c++
#include <iostream>
#include <memory>
#include <unordered_map>
#include <cstring>

class Cach{
  std::unordered_map<std::string, std::weak_ptr<int>> cache;
public:
  std::shared_ptr<int> get(const std::string& key) {
    auto it = cache.find(key);
    if (it != cache.end()) {
      std::shared_ptr<int> sp = it->second.lock();
      if (sp) {
        return sp;
      } else {
        cache.erase(it);
      }
    }
    return nullptr;
  }
  void add(const std::string& key, std::shared_ptr<int> value) {
    cache[key] = value;
  }
};

int main() {
  Cache cache;
  auto sp1 = std::make_shared<int>(42);
  cache.add("answer", sp1);
  {
    auto sp2 = cache.get("answer");
    if (sp2) {
      std::cout << "Cached value:" << *sp2 << std::endl;
    } else {
      std::cout << "Value not in cache" << std::endl;
    }
  }
  sp1.reset();
  {
    auto sp2 = cache.get("answer");
    if (sp2) {
      std::cout << "Cached value:" << *sp2 << std::endl;
    } else {
      std::cout << "Value not in cache" << std::endl;
    }
  }
  return 0;
}
~~~





----

stl 底层问题

- 如何实现 std::vector 的动态拓展机制，其拓展策略是怎么样的

vector 本质就是一个动态数组，它实现包括一个指向动态内存分配的指针、当前大小和当前容量。当 vector 中添加元素超过其当前容量时候，vector 会将现有元素赋值到新内存块中，然后释放旧内存块中。拓展策略通常是将容量翻倍，以摊销插入操作的时间复杂度。

- vector 和 deque 的底层实现有什么不同，他们的时间复杂度区别是什么

vector 是 动态数组，连续存储所有元素，而 deque 是双端队列 通常由多个固定大小的快组成，支持快速的头尾插入和删除。vector 的插入或删除非尾部元素的时间复杂度为 O(N) 而 deque 可以在 O(1) 时间内进行头尾插入和删除 随机访问时间复杂度也为 O(1)

什么场景下应该优先使用 deque 而不是 vector 呢？

- list 是单向列表还是双向链表

list 是双向链表允许在常数时间内进行插入和删除操作。

- map 和 unordered_map 的底层实现区别是什么

map 底层实现是 红黑树 或者 平衡二叉树的有序关联容器，支持按顺序遍历。unordered_map 是基于哈希表的无序关联容器，支持快速查找、插入和删除操作。



STL的定制化，如何写？写一个节点，给出一个rank多少。一个因子，就是要给出这个股票他在所有股票中的rank是多少。本质是一个map来实现。加一个额外值，左子树和右子树进行一个数的维护，递归维护即可。updates red black trees （里面会存一些update method）



插入大量数据时，unordered_map 可能面临什么问题，如何解决

- unique_str 的实现原理是什么，它如何确保独占所有权

unique_ptr 通过禁止拷贝构造和赋值操作来确保独占所有权，只允许移动构造和移动赋值

什么时候应该使用自定义删除器，如何实现

- allocator 的作用是什么，如何自定义一个 allocator

allocator 是 stl 中用于内存分配和释放的类，可以通过自定义分配器来控制内存



类型比较死板，比如说rbtree 的allocator，allocate的是node，不止是value，其实还有key



std::allocator 是 c++ 标准库中的一个类模板，用于定义对象的内存分配策略。它是标准库容器如 std::vector std::list std::map 默认使用的内存分配器

主要功能 allocator 提供了一些方法来管理内存，包括分配内存、释放内存、构造对象、销毁对象，其主要成员函数包括：

allocate(size_t n) 分配能够容纳 n 个 类型为 T 的对象的未初始化存储空间

deallocate(T* p, size_t n) 释放之前分配的内存

construct(T* p, Args&& ... args) 在分配的内存中构造对象

destroy(T* p) 调用对象的析构函数

~~~c++
template<typename T>
struct MyAllocator {
  typedef T value_type;
  MyAllocator() = default;
  template<teypename U>
  MyAllocator(constt MyAllocator<U>&) {}
 	T* allocate(std::size_t n) {
    return static_cast<T*>(::operator new(n * sizeof(T)));
  }
  void deallocate(T* p, std::size_t) {
    ::operator delete(p);
  }
}
~~~

什么情况下需要自定义 allocator

- string 是如何管理内存的，它的 small string optimization 机制是怎么样的

string 管理内存时使用动态分配来存储字符串数据。sso 是一种优化技术，当字符串长度小于一定值时候，字符串存储在 string 对象内部缓冲区中，而不尽兴动态分配，以提高性能和减少内存分配的开销

sso 的具体实现和存储策略是怎么样的，他会对哪些操作带来性能提升

- algorithm 中的 sort 使用了哪种排序算法，它是如何选择不同的排序策略的

sort 通常使用 快速排序，但为避免最坏情况下的 O(N^2) 时间复杂度，他在实现中结合了插入排序和堆排序 来优化性能，即三路切分快速排序

为什么插入排序能够优化小数据集？其时间复杂度和空间复杂度是多少？

- priority_queue 底层实现是什么如何实现其堆结构

priority_queue 通常基于 vector 实现最大堆或最小堆，插入和删除操作通过堆的上滤和下滤维护堆的性质

如何自定义 priority_queue 的排序顺序（如何实现一个 cmp function）

- bitset 是什么，它如何实现高效的位操作，它和 vector<bool> 有什么区别

bitset 使用固定大小的位数组来存储二进制位，高效的支持按位操作

vector of bool 使用压缩存储，每个布尔值占用1位，但不提供与 vector 相同的借口和性能

- mutex 和 shared_mutex 底层实现及区别是什么

mutex 提供独占锁，防止多个线程同时访问临界区；shared_mutex 支持共享锁和独占锁，允许多个线程同时读取，但写操作需要独占锁，shared mutex 使用读者-写着机制

- future 和 promise 是如何实现异步任务的，他们的底层机制是什么

future 和 promise 通过共享状态实现异步任务。promise 设置共享状态的值，future 获取该值，通过 async 创建异步任务，使用条件变量和互斥锁来实现线程间通信

~~~c++
std::promise<int> prom;
std::future<int> fut = prom.get_future();
std::thread([](std::promise<int> prom) {prom.set_value(10)}, std::move(prom)).detach();
~~~

- 如何实现一个高效的 hash 函数，如何避免哈希冲突

一个高效的 hash 函数应该均匀分布数据输入，减少冲突。通常通过组合多个哈希函数或使用更复杂的哈希算法来实现。避免冲突可以通过开放地址法或链地址法来处理

如何实现自定义类型的哈希函数，给出例子

- tuple 是如何实现类型安全的多值返回的，其底层原理是什么

tuple 使用模版和参数包实现类型安全的多值返回，通过递归继承和索引访问元素，每个元素类型在编译时确定，确保类型安全。

~~~c++
std::tuple<int, std::string, double> tpl = std::make_tuple(1, "hello", 3.14);
~~~

- any 如何存储任意类型的数据，他的类型安全是如何实现的

any 使用类型擦出和动态分配存储任意类型的数据，通过 type_info 实现类型安全，存储数据的类型信息以确保安全的类型转换

~~~c++
std::any a = 10;
int b = std::any_cast<int>(a);
~~~

- variant 如何实现类型安全的多态，他和 any 的区别是什么

variant 是一种联合类型，支持多种类型的安全存储和访问，通过访问索引或类型获取存储值。与 any 不同， variant 的类型在编译时确定，更高效且无类型信息存储开销。

~~~c++
std::variant<int, std::string> var = "hello";
~~~

variant 能够提供多种类型存储的值，可以存储指定的一组类型中的任意一种类型

~~~c++
std::variant<int, std::string> v1;
std::variant<int, std::string> v2 = 42;
std::variant<int, std::string> v3 = "hello"
~~~

访问存储的值，使用 std::get

std::visit 访问 std::variant 中的值要如何访问



- optional 是如何实现值的存在性检查的，他的底层实现原理是什么

optional 通过一个布尔标志位和一个联合类型来实现值的存在性检查，如果值存在，则标志位为真，并存储值，否则标志位为假，不存储值

如何使用 std::optional 处理函数的返回值？

用于表示函数可能返回值或可能不返回值的情况，例如查找函数可能返回找到的元素也可能返回空：

~~~c++
std::optional<std::string> findValue(const std::vector<std::string>& vec, const std::string& target) {
  for (const auto& item: vec) {
    if (item == target) {
      return item;
    }
  }
  return std::nullopt;
}
~~~

用法2 延迟初始化，在某些情况下，需要对初始化对象之前进行某些计算或检查，std::optional 可以用于延迟初始化

~~~c++
std::optional<int> computeValue (bool condition) {
	if (condition) {
    return 42;
  }
  else {
    return std::nullopt;
  }
}
~~~



----

c++ 源码

cmath 源码

https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/c_std/cmath

vector源码

https://github.com/steveLauwh/SGI-STL/blob/master/The%20Annotated%20STL%20Sources%20V3.3/container/sequence%20container/vector/stl_vector.h

原版的 m_insert_aux 函数，push_back 和 insert 都是基于 m_insert_aux 函数之上进行封装的

~~~c++
template<class _Tp, class _Alloc>
void vector<_Tp, _Alloc>::_M_insert_aux(iterator __position, const _Tp& __x) {
  if (_M_finish != _M_end_of_storage) {
    construct(_M_finish, *(_M_finish - 1));
    ++_M_finish;
    _Tp __x_copy = __x;
    copy_backward(__position, _M_finish - 2, _M_finish - 1);
    *__position = __x_copy;
  }
  else { // no backup space
    const size_type __old_size = size();
    const size_type __len = __old_size != 0 ? 2 * __old_size : 1;
    iterator __new_start = _M_allocate(__len);
    iterator __new_finish = __new_start;
    __STL_TRY {
      __new_finish = uninitialized_copy(_M_start, __position, __new_start);
      construct(__new_finish, __x);
      ++__new_finish;
      __new_finish = uninitialized_copy(__position, _M_finish, __new_finish);
    }
    __STL_UNWIND((destroy(__new_start,__new_finish), 
                  _M_deallocate(__new_start,__len)));
    destroy(begin(), end());
    _M_deallocate(_M_start, _M_end_of_storage - _M_start);
    _M_start = __new_start;
    _M_finish = __new_finish;
    _M_end_of_storage = __new_start + __len;
  }
}
~~~

~~~c++
/*
Attributes:
_M_start // begin iterator
_M_finish // end iterator
_M_end_of_storage // storage end iterator
copy_backward( , , ) // copy memory

*/
template<class _Tp, class _Alloc>
void vector<_Tp, _Alloc>::_M_insert_aux(iterator __position, const _Tp& __x) {
  if (_M_finish != _M_end_of_storage) {
    // 1. construct _M_finish
    // 2. copy backward part
    // 3. insert __x into __position
  }
  else { // no enough backup space
    // 1. use allocator to initiliaze new memory (before x part, after x part)
    // 2. destroy previous memory
    // 3. redefine iterators
  }
}
~~~

~~~c++
template<class _Tp, class _Alloc>
void vector<_Tp, _Alloc>::_M_insert_aux(iterator __position, const _Tp& __x) {
  if (_M_finish != _M_end_of_storage) {
  }
  else {
  }
}
~~~





----

代码问题，实现一个 time_series_rolling_median 的函数，要求是会删除的，随着时间rolling滚动的





-----

c++ template 高级模板编程技术 SFINAE substitution failure is not an error 

1. SFINAE Substitution Failure is Not an Error

SFINAE 是 C++ 模板编程中的一项重要特性。当编译器在实例化模板时，如果遇到模板参数替换失败（比如替换结果不是合法的类型或表达式），编译器不会报错，而是会回退到其他模板匹配。这使得可以通过模板实现条件编译和选择性地实例化模板。示例：**检测类型是否有特定成员函数**

2. std::enable_if 

是一个在 C++11 引入的工具，用于在编译期启用或禁用某些模板。这通常与 SFINAE 一起使用，用于条件编译。示例：**根据类型特性启用或禁用函数模板**

3. 变参模板 Variadic Templates

变参模板允许定义接受可变数量参数的模板。这在需要处理任意数量的模板参数时非常有用 示例：**递归打印任意数量的参数**

~~~c++
#include <iostream>
void print() {
  std::cout << std::endl;
}

template <typename T, typename... Args>
void print(T first, Args... args) {
  std::cout << first << " ";
  print(args...);
}
int main() {
  print(1, 2.5, "Hello", 'A');
  return 0;
}
~~~

4. 模板特化 Template Specialization

模板特化允许为特定的类型或条件提供不同的实现。这可以是完全特化（为特定类型提供实现）或者部分特化（为满足特定条件的类型提供实现）示例 **完全特化**

5. Type Traits

Type Traits 是一组模板，用于在编译期间查询类型信息和特性。标准库中有许多现成的 Type Traits，比如 std::is_integral， std::is_floating_point 等 示例 **使用 Type Triats 进行类型判断**







虚函数慢，编译级别的优化无法做，但是静态，模板来做，就是会快很多。代码会暴露。

simd 指令集的了解：批量计算，cpu最喜欢一个长数组，cpu是一批一批数据算过去的。树形结构不行，必须是数组结构。























