t = int(input())
people = [[1] for _ in range(15)]
people[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(1, 15):
    for j in range(1, 14):
        people[i].append(people[i][j-1]+people[i-1][j])
    
for _ in range(t):
    k = int(input())
    n = int(input())
    print(people[k][n-1])