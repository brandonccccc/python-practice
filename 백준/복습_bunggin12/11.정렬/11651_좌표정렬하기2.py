import sys

n = int(input())
point_list = []
for _ in range(n):
    point_list.append(list(map(int, input().split())))
point_list.sort(key = lambda x:(x[1],x[0]))
for i in point_list:
    print(*i)