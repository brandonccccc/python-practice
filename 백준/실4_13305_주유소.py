import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
o = list(map(int, input().split()))

answer = s[0] * o[0]
oil = o[0]
for i in range(1, n-1):
    if o[i] < oil:
        oil = o[i]
    answer += s[i]*oil

print(answer)