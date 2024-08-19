什么是 cache?

- cache 是一种高速寄存器，用于临时存储数据和指令，以减少对较慢存储设备的访问次数，从而提高数据反问速度。它基于局部性原理，包括时间局部性和空间局部性

cache 的工作原理是什么？

- cache 的工作原理基于局部性原理。当处理器需要访问数据时，它会首先检查缓存，如果数据在 cache 中，则可以直接快速获取数据；如果不在 cache 中（cache 未命中），则需要从主存储器或者更慢的设备中获取数据，并将其加载到缓存中，以便后续访问

cache 的级别有哪些

- cache 通常分为多级，例如 L1 一级缓存、L2 二级缓存、L3 三级缓存。级别越低，容量越小，速度越快，成本越高

什么是缓存命中和缓存未命中

- cache hit 是指当处理器需要访问数据时，所需的数据已经在缓存中，可以直接快速获取。缓存未命中 cache miss 是指所需的数据不在缓存中，需要从主存储器或者更慢的设备中获取数据，并加载到缓存中

缓存的替换策略有哪些

- lru least recently used，替换最长时间未被使用的数据
- fifo first in first out，替换最先进入缓存的数据
- 随机替换 random，随机选择一个数据进行替换
- lfu least frequently used，替换访问次数最少的数据

缓存的写策略有哪些

- 写直达 write-through，每次写操作都同时写入缓存和主存储器
- 写回 write-back，每次写操作只写入缓存，当数据被替换出缓存时，才写回主存储器
- 写分配 write-allocate，当发生写未命中时，直接将数据写入主存储器，不加载到缓存中