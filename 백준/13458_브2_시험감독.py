import sys
import math
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for i in range(n):
    student[i] -= b
    answer += 1
    if student[i] > 0:
        answer += math.ceil(student[i]/c)

print(answer)