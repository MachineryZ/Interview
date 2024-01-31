/*
设计一个简单的内存分配器，实现 malloc 和 free 的功能
要求：
1. 内存分配器能够管理一个固定大小的内存池
2. 实现 void* malloc（size_t size）的函数，接受一个需要分配的字节数，返回一个指向分配的内存块的指针，如果没有足够的可用内存，则返回 NULL
3. 实现 void free（void* ptr）函数，接受一个指向之前分配的内存块的指针，将该内存块释放，使其可重新使用
4. 考虑内存对齐的问题，确保分配的内存块满足特定的对齐要求
5. 考虑内存碎片化的问题，尽量减少内存碎片的产生
6. 内存分配器需要管理内存块的分配和释放，以便有效的利用内存池

在构造函数中，我们使用 std::malloc 函数分配制定大小的内存池，并将其转化为MemoryBlock 结构体的指针。然后我们初始化了第一个内存块 firstBlock，指定他的大小
为内存池大小减去 MemoryBlock 结构体的大小，并将其标记为可用 free = true

allocate 函数用于分配内存，它便利内存块链表，查找第一个可用且大小足够的内存块，如果找到了合适的内存块，我们将其分割成两个块；一个用于分配，
另一个用于剩余的空间内存。然后我们标记分配的内存块为不可用，并返回指针

free 函数用于释放先前分配的内存块，它接受一个指向分配内存块的指针，将其转换为MemoryBlock结构体的指针，并将其标记为可用。然后，我们合并相邻的空闲
内存块，以减少内存碎片化

在 main 函数中，我们使用 MemoryAllocator 类来分配一个整型变量的内存，将其设置为 42，并输出结果。然后，我们使用 free 函数释放先前分配的内存
*/

#include <iostream>
#include <cstddef>

class MemoryAllocator {
private:
    struct MemoryBlock {
        size_t size;
        bool free;
        MemoryBlock* next;
        MemoryBlock* prev;
    };

    void* memoryPool;
    MemoryBlock* firstBlock;

public:
    MemoryAllocator(size_t poolsize) {
        memoryPool = std::malloc(poolsize);
        firstBlock = reinterpret_cast<MemoryBlock*>(memoryPool);
        firstBlock->size = poolsize - sizeof(MemoryBlock);
        firstBlock->free = true;
        firstBlock->next = nullptr;
        firstBlock->prev = nullptr;
    }

    ~MemoryAllocator() {
        std::free(memoryPool);
    }

    void* allocate(size_t size) {
        MemoryBlock* currentBlock = firstBlock;
        while (currentBlock) {
            if (currentBlock->free and currentBlock->size >= size) {
                splitBlock(currentBlock, size);
                currentBlock->free = false;
                return reinterpret_cast<void*>(currentBlock + 1);
            }
            currentBlock = currentBlock->next;
        }
        return nullptr;
    }

    void free(void* ptr) {
        if (!ptr)
            return;

        MemoryBlock* blockToFree = reinterpret_cast(MemoryAllocator);
        blockToFree->free = true;
        mergeBlocks(blackToFree);
    }
private:
    void splitBlock(MemoryBlock* block, size_t size) {
        if (block->size > size + sizeof(MemoryBlock)) {
            MemoryBlock* newBlock = reinterpret_cast<MemoryBlock*>(reinterpret_cast<char*>(block + 1) + size);
            newBlock->size = block->size - size - sizeof(MemoryBlock);
            newBlock->free = true;
            newBlock->next = block->next;
            newBlock->prev = block;
            if (block->next)
                block->next->prev = newBlock;
            block->next = newBlock;
            block->size = size;
        }
    }
    void mergeBlocks(MemoryBlock* block) {
        if (block->next and block->next->free) {
            block->size += block->next->size + sizeof(MemoryBlock);
            block->next = block->next->next;
            if (block->next)
                block->next->prev = blocks;
        }
        if (block->prev and block->prev->free) {
            block->prev->size += block->size + sizeof(MemoryBlock);
            block->prev->next = block->next;
            if (block->next)
                block->next->prev = block->prev;
            block = block->prev;
        }
    }
};

int main() {
    MemoryAllocator allocator(1024);

    int* num = static_cast<int*>(allocator.allocate(sizeof(int)));
    *num = 42;
    std:: << *num << std::endl;
    allocator.free(num);
    return 0;
}

/*
对于更复杂的内存分配器，可以考虑一下算法和数据结构来提高性能和处理更复杂的情况
1. 分离适配 segregated fit：将内存块按照大小分类，维护多个内存块链表，
    每个链表专门用于存储一定大小范围内的内存块。这样可以减少内存碎片化，并提高内存分配的效率
2. 伙伴系统 buddy system：将内存分割成固定大小的块，并按照 2 的幂次进行分级。每个级别的
    内存块都有一个伙伴块，两个相邻的伙伴块可以合并成更大的内存块。这个系统可以提供较好的
    内存利用率，但需要额外的数据结构来管理伙伴系统。
    可以使用的数据结构是：bitmap 和 free list
3. 位图 bitmap：使用位图来表示内存块的使用情况，每个位表示一个内存块的状态 分配或者空闲。位图
    可以在较小的空间内快速查找可用的内存块，但需要考虑位图的管理和更新
4. 内存池的扩展和缩小：当需要分配更大的内存块时，可以将多个相邻的空闲内存块合并成一个更大的内存块。
    当释放内存时，可以将较大的内存块分割成多个较小的内存块。这可以减少内存碎片化，并提高内存块的重用率
5. 预分配策略：提前分配一部分内存块，以减少分配内存的时间开销。可以使用预分配池来存储预先分配的内存块，并
    在需要时直接从池中获取
6. 内存池的动态扩展和收缩：根据内存使用情况动态调整内存池的大小。当内存不足时，可以动态扩展内存池；当内存
    闲置较多时，可以收缩内存池以释放系统资源
*/