N = int(input())
count = N - 1

for i in range(1, 2*N):
    if i <= N:
        print(str("*"*i).ljust(N),end = "")
        print(str("*"*i).rjust(N))
    else:
        print(str("*"*count).ljust(N),end="")
        print(str("*"*count).rjust(N))
        count -= 1



"""
for i in range(0,N):
    print("*"*count)
    count -= 1
    

for i in range (1, N+1):
    print("*"*i)
    
for i in range (1, N+1):
    print(str("*"*i).rjust(N))"""