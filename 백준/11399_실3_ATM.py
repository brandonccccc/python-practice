import sys
input = sys.stdin.readline

n = int(input())
pi = list(map(int, input().split()))
pi.sort() # 빠른 순으로 정렬
answer = 0
for i in range(len(pi)):
    answer += pi[i] * (n-i)  #앞 순번이 걸리는 시간이 가장 여러번 더해짐

print(answer)