N = int(input())

for i in range (1, N+1):
    print(str("*"*i).rjust(N))

    # str(x).rjust(n) x라는 문자열을 n칸에 대해서 오른쪽 정렬
    # ljust는 왼쪽 정렬