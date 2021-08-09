N = int(input())
count = N
for i in range(0,N):
    print(str("*"*count).rjust(N))
    count -= 1