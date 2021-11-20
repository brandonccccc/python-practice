import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)  # 내림차순 정렬을 위해서 -value 를 heappush
    for i in range(len(h)):
        result.append(heapq.heappop(h))  # 내림차순 정렬을 위해서 -heapq.heappop
    return result

result = heapsort([3, 2, 9, 8, 5, 4, 1, 6, 7, 0])
print(result)

