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