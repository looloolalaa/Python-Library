import heapq

if __name__ == '__main__':
    # min_heap
    h = []
    heapq.heappush(h, (4, 'what'))
    heapq.heappush(h, (3, ['d']))
    heapq.heappush(h, (1, 4444))
    heapq.heappush(h, (2, (11, 1)))
    while h:
        print(heapq.heappop(h))
    print()

    # max_heap
    heapq.heappush(h, (-4, 'what'))
    heapq.heappush(h, (-3, ['d']))
    heapq.heappush(h, (-1, 4444))
    heapq.heappush(h, (-2, (11, 1)))
    while h:
        print(heapq.heappop(h))
    print()

    # heapify
    h = [(4, 'what'), (3, ['d']), (1, 4444), (2, (11, 1))]
    heapq.heapify(h)
    while h:
        print(heapq.heappop(h))