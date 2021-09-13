import sys
A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
Am = list(map(int, sys.stdin.readline().split()))
Am.reverse()
sum = 0
ans = []

for i in range(m):
    sum += (A ** i) * (Am[i])
    
while sum:
    if sum // B:
        ans.append(sum % B)
        sum = sum // B
    else:
        ans.append(sum)
        ans.reverse()
        break
for i in range(len(ans)):
    print(ans[i],end=' ')