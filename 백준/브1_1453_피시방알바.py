n = int(input())
pc = [0] * 101
cnt = 0
people = [i for i in map(int, input().split())]

for i in range(n):
    if pc[people[i]] == 0:
        pc[people[i]] = 1
    else:
        cnt += 1

print(cnt)