q = input()
print(q)
print(type(q))

print(*q)

from collections import deque
q = [1,2,3,4]

def reverse_list(array):
    if len(array) <= 1:
        return array
    return array[-1:] + reverse_list(array[:-1])

print(reverse_list(q))