import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    data1 = list(map(int, input().split()))
    data1.sort()
    m = int(input())
    data2 = list(map(int, input().split()))

    for i in data2:
        result = binary_search(data1, i, 0, n-1)
        print(result)
