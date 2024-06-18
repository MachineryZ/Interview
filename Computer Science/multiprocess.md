生产者消费者

1. **生产者-消费者问题**
   - **描述**：生产者进程生成数据，并将数据放入缓冲区中。消费者进程从缓冲区中取出数据进行处理。需要确保生产者不会在缓冲区满时继续生成数据，而消费者不会在缓冲区空时继续取数据。
   - **考点**：进程同步、信号量、共享缓冲区。

~~~python
import multiprocessing
import time
import random

def producer(queue):
    while True:
        item = random.randint(1, 100)
        queue.put(item)
        print(f'Produced {item}')
        time.sleep(random.random())

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Sentinel value to terminate consumer
            break
        print(f'Consumed {item}')
        time.sleep(random.random())

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    try:
        time.sleep(5)  # Let the processes run for a while
    finally:
        queue.put(None)  # Stop the consumer
        producer_process.terminate()
        consumer_process.join()
        producer_process.join()
~~~

哲学家进餐问题

1. **哲学家进餐问题**
   - **描述**：五位哲学家围坐在圆桌旁，每位哲学家需要轮流进餐和思考，桌上有五根筷子。哲学家只有在左右两根筷子都可用时才能进餐。如何避免死锁和饥饿问题？
   - **考点**：进程同步、死锁预防、资源分配。

~~~python
import multiprocessing
import time
import random

def philosopher(philosopher_id, left_fork, right_fork):
    while True:
        time.sleep(random.uniform(1, 3))  # Thinking
        with left_fork:
            with right_fork:
                print(f'Philosopher {philosopher_id} is eating.')
                time.sleep(random.uniform(1, 2))  # Eating

if __name__ == '__main__':
    num_philosophers = 5
    forks = [multiprocessing.Lock() for _ in range(num_philosophers)]
    philosophers = []

    for i in range(num_philosophers):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % num_philosophers]
        philosopher_process = multiprocessing.Process(target=philosopher, args=(i, left_fork, right_fork))
        philosophers.append(philosopher_process)
        philosopher_process.start()

    time.sleep(10)  # Let the philosophers dine for a while

    for philosopher_process in philosophers:
        philosopher_process.terminate()
        philosopher_process.join()

~~~

读者-写者问题

1. **读者-写者问题**
   - **描述**：允许多个读者同时读取共享数据，但只允许一个写者修改数据。如何确保读写操作的正确性，防止读写冲突？
   - **考点**：进程同步、读写锁、优先级处理。

~~~python
import multiprocessing
import time
import random

def reader(reader_id, rw_lock):
    while True:
        rw_lock.acquire_read()
        print(f'Reader {reader_id} is reading.')
        time.sleep(random.uniform(1, 2))  # Reading
        rw_lock.release_read()
        time.sleep(random.uniform(1, 3))  # Thinking

def writer(writer_id, rw_lock):
    while True:
        rw_lock.acquire_write()
        print(f'Writer {writer_id} is writing.')
        time.sleep(random.uniform(1, 2))  # Writing
        rw_lock.release_write()
        time.sleep(random.uniform(2, 4))  # Thinking

class ReadWriteLock:
    def __init__(self):
        self.lock = multiprocessing.Lock()
        self.readers = 0
        self.writer_lock = multiprocessing.Lock()

    def acquire_read(self):
        with self.lock:
            self.readers += 1
            if self.readers == 1:
                self.writer_lock.acquire()

    def release_read(self):
        with self.lock:
            self.readers -= 1
            if self.readers == 0:
                self.writer_lock.release()

    def acquire_write(self):
        self.writer_lock.acquire()

    def release_write(self):
        self.writer_lock.release()

if __name__ == '__main__':
    rw_lock = ReadWriteLock()

    readers = [multiprocessing.Process(target=reader, args=(i, rw_lock)) for i in range(3)]
    writers = [multiprocessing.Process(target=writer, args=(i, rw_lock)) for i in range(2)]

    for r in readers:
        r.start()
    for w in writers:
        w.start()

    time.sleep(10)  # Let the readers and writers work for a while

    for r in readers:
        r.terminate()
        r.join()
    for w in writers:
        w.terminate()
        w.join()

~~~

烟民问题

- 三个烟民和一个代理人，代理人提供三种原料（烟草、纸、火柴）中的两种，每个烟民缺少一种原料。烟民需要等待自己缺少的原料出现，然后卷烟并抽烟。
- **考点**：进程同步、信号量、条件变量。

~~~python
import multiprocessing
import time
import random

def smoker(smoker_id, item_needed, items):
    while True:
        item1, item2 = items.get()
        if item_needed not in [item1, item2]:
            print(f'Smoker {smoker_id} is smoking with items {item1} and {item2}.')
            time.sleep(random.uniform(1, 2))  # Smoking
        else:
            items.put((item1, item2))  # Put items back if not needed

def agent(items, all_items):
    while True:
        time.sleep(random.uniform(1, 2))
        item1, item2 = random.sample(all_items, 2)
        print(f'Agent puts items {item1} and {item2}.')
        items.put((item1, item2))

if __name__ == '__main__':
    items = multiprocessing.Queue()
    all_items = ['tobacco', 'paper', 'matches']

    smokers = [multiprocessing.Process(target=smoker, args=(i, all_items[i], items)) for i in range(3)]
    for s in smokers:
        s.start()

    agent_process = multiprocessing.Process(target=agent, args=(items, all_items))
    agent_process.start()

    time.sleep(10)  # Let the smokers and agent work for a while

    for s in smokers:
        s.terminate()
        s.join()
    agent_process.terminate()
    agent_process.join()

~~~

并行排序 归并排序

1. **并行排序**
   - **描述**：使用多进程实现并行排序算法，如归并排序或快速排序，比较与单线程版本的性能差异。
   - **考点**：并行计算、进程同步、性能优化。

~~~python
import multiprocessing

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    with multiprocessing.Pool(2) as pool:
        left, right = pool.map(parallel_merge_sort, [left, right])

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = parallel_merge_sort(arr)
    print(f'Sorted array: {sorted_arr}')

~~~

























