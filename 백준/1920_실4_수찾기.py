import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input().rstrip())
A = []
for i in map(int, input().split()):
    A.append(i)
A.sort()

m = int(input().rstrip())
array = list(map(int, input().split()))

for i in array:
    result = binary_search(A, i, 0, n-1)
    if result != None:
        print(1)
    else:
        print(0)
