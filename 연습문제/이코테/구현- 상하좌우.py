T = int(input())
command = list(input().split())
loc = [1, 1]

for i in range(len(command)):
    if command[i] == 'R' and loc[1] <= T:
        loc[1] += 1
    elif command[i] == 'U' and loc[0] > 1:
        loc[0] -= 1
    elif command[i] == 'D' and loc[0] <= T:
        loc[0] += 1
    elif command[i] == 'L' and loc[1] > 1:
        loc[1] -= 1
for i in range(2):
    print(loc[i], end=' ')