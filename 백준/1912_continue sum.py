n = int(input())
A = list(map(int, input().split()))
sum = [A[0]]
for i in range(n-1):
    sum.append(max(sum[i]+A[i+1], A[i+1]))
print(max(sum))