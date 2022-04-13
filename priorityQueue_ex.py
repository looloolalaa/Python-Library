from queue import PriorityQueue
import heapq

if __name__ == '__main__':
    # 1. min_heap
    h = []
    heapq.heappush(h, 4)
    heapq.heappush(h, 5)
    heapq.heappush(h, 1)
    # [1, 5, 4]
    heapq.heappop(h)  # 1
    # [4, 5]


    # 2. max_heap
    temp = [10, 40, 50]
    h = []
    result = []
    for i in temp:
        heapq.heappush(h, -i)
    while h:
        result.append(-heapq.heappop(h))
    print(result)


    # PriorityQueue
    que = PriorityQueue()
    que.put((4, 'middle'))
    que.put((5, 'five'))
    que.put((1, 'first'))
    que.put((8, 'low'))
    # [(1, 'first'), (4, 'middle'), (5, 'five'), (8, 'low')]
    print(que.get())
    print(que.get())
    print(que.qsize())
    print(que.empty())
