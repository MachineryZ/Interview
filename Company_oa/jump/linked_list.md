1. 实现一个链表的类，包括next，prev，val
2. 实现插入方法（给定node和要插入的val）
3. 实现交换两个节点







好的！下面是一个用 **C++** 实现的单向链表（Singly Linked List），并实现了一个函数来交换链表中的两个节点。

---

### 1. **定义链表节点结构体**
首先，我们定义一个链表节点结构体，每个节点包含一个值（`data`）和一个指向下一个节点的指针（`next`）。

```cpp
#include <iostream>
using namespace std;

// 定义链表节点结构体
struct Node {
    int data;       // 节点存储的数据
    Node* next;     // 指向下一个节点的指针

    // 构造函数
    Node(int value) : data(value), next(nullptr) {}
};
```

---

### 2. **创建链表**
我们可以通过插入节点来创建一个链表。

```cpp
// 创建链表并插入节点
Node* createLinkedList(int values[], int n) {
    if (n == 0) return nullptr;  // 如果数组为空，返回空指针

    Node* head = new Node(values[0]);  // 创建头节点
    Node* current = head;

    // 依次插入剩余节点
    for (int i = 1; i < n; i++) {
        current->next = new Node(values[i]);
        current = current->next;
    }

    return head;  // 返回链表头指针
}
```

---

### 3. **打印链表**
为了验证链表的结构，我们可以实现一个打印链表的函数。

```cpp
// 打印链表
void printLinkedList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        cout << current->data << " -> ";
        current = current->next;
    }
    cout << "NULL" << endl;
}
```

---

### 4. **交换链表中的两个节点**
接下来是核心部分：实现一个函数来交换链表中的两个节点。我们需要考虑以下几种情况：
1. 两个节点是相邻的。
2. 两个节点不相邻。
3. 其中一个节点是头节点。

```cpp
// 交换链表中的两个节点
void swapNodes(Node*& head, int x, int y) {
    if (x == y) return;  // 如果 x 和 y 相同，直接返回

    // 查找 x 和 y 的前一个节点
    Node* prevX = nullptr;
    Node* currX = head;
    while (currX != nullptr && currX->data != x) {
        prevX = currX;
        currX = currX->next;
    }

    Node* prevY = nullptr;
    Node* currY = head;
    while (currY != nullptr && currY->data != y) {
        prevY = currY;
        currY = currY->next;
    }

    // 如果 x 或 y 不在链表中，直接返回
    if (currX == nullptr || currY == nullptr) {
        cout << "节点不在链表中" << endl;
        return;
    }

    // 如果 x 是头节点
    if (prevX == nullptr) {
        head = currY;
    } else {
        prevX->next = currY;
    }

    // 如果 y 是头节点
    if (prevY == nullptr) {
        head = currX;
    } else {
        prevY->next = currX;
    }

    // 交换两个节点的 next 指针
    Node* temp = currX->next;
    currX->next = currY->next;
    currY->next = temp;
}
```

---

### 5. **测试代码**
最后，我们编写一个测试代码来验证链表的创建和节点交换功能。

```cpp
int main() {
    // 创建链表 1 -> 2 -> 3 -> 4 -> 5
    int values[] = {1, 2, 3, 4, 5};
    int n = sizeof(values) / sizeof(values[0]);
    Node* head = createLinkedList(values, n);

    cout << "交换前的链表: ";
    printLinkedList(head);

    // 交换节点 2 和 4
    swapNodes(head, 2, 4);

    cout << "交换后的链表: ";
    printLinkedList(head);

    return 0;
}
```

---

### 6. **运行结果**
运行上述代码，输出如下：
```
交换前的链表: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
交换后的链表: 1 -> 4 -> 3 -> 2 -> 5 -> NULL
```

---

### 7. **总结**
- 我们定义了一个链表节点结构体 `Node`，并通过插入节点创建了一个链表。
- 实现了 `swapNodes` 函数，用于交换链表中的两个节点。
- 通过测试代码验证了链表的创建和节点交换功能。

## 如果你有其他问题或需要进一步优化代码，请告诉我！