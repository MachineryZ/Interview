/*
设计一个简单的内存分配器，实现 malloc 和 free 的功能
要求：
1. 内存分配器能够管理一个固定大小的内存池
2. 实现 void* malloc（size_t size）的函数，接受一个需要分配的字节数，返回一个指向分配的内存块的指针，如果没有足够的可用内存，则返回 NULL
3. 实现 void free（void* ptr）函数，接受一个指向之前分配的内存块的指针，将该内存块释放，使其可重新使用
4. 考虑内存对齐的问题，确保分配的内存块满足特定的对齐要求
5. 考虑内存碎片化的问题，尽量减少内存碎片的产生
6. 内存分配器需要管理内存块的分配和释放，以便有效的利用内存池
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

    void free()
}