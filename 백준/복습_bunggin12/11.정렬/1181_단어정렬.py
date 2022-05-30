import sys
input = sys.stdin.readline

n = int(input())
str_list = []
for _ in range(n):
    str_list.append(input().rstrip())
str_list = list(set(str_list))
str_list.sort()
str_list.sort(key = lambda x: len(x))
for i in str_list:
    print(i)