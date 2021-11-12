n = int(input())
members = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    members[i] = x, y
for i in members:
    rank = 1
    for j in members:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    
    print(rank, end= ' ')