N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]
dp_up = [1] * N
dp_down = [1] * N
sum = []
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)
        if reverse_A[i] > reverse_A[j]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)
for i in range(0, N):
    sum.append(dp_down[N-i-1]+dp_up[i])
print(max(sum)-1)