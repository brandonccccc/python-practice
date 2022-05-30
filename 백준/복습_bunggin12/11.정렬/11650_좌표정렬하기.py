import sys

n = int(input())
point_list = []
for _ in range(n):
    point_list.append(list(map(int, input().split())))
"""for i in range(n):
    for j in range(i+1, n):
        if point_list[i][0] > point_list[j][0]:
            point_list[i], point_list[j] = point_list[j], point_list[i]
        elif point_list[i][0] == point_list[j][0] and point_list[i][1] > point_list[j][1]:
            point_list[i], point_list[j] = point_list[j], point_list[i]"""

point_list.sort(key = lambda x:(x[0],x[1]))
for i in point_list:
    print(*i)