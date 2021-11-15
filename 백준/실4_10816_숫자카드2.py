import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in numbers:
    if i in dic:
        print(dic[i], end = ' ')
    else:
        print(0, end = ' ')
