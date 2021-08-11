N = int(input())
count = N - 1

for i in range(1, 2*N):
    if i <= N:
        print(str("*"*i).rjust(N))
    else:
        print(str("*"*count).rjust(N))
        count -= 1
