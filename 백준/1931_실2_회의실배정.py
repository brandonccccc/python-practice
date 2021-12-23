import sys
input = sys.stdin.readline

n = int(input())
conf = []
for _ in range(n):
    conf.append(list(map(int, input().split())))

conf.sort(key = lambda x:(x[1], x[0]))

cnt = 1
end_time = conf[0][1]
for i in range(1, n):
    if conf[i][0] >= end_time:
        cnt+=1
        end_time = conf[i][1]
        
print(cnt)