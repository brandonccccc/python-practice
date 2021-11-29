import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
answer = 0
for i in range(len(a)):
    answer += a[i]*max(b)
    b.remove(max(b))
    
print(answer)