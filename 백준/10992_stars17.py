N = int(input())
for i in range(N):
    if i == 0:
        print(str("*").center(2*N-1))
    elif i == N-1:
        print(str("*"*(2*N-1)).center(2*N-1))
    else:
        print(str("*" + " "*(2*i-1) + "*").center(2*N-1))