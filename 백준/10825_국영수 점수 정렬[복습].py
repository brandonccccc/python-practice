"""N = int(input())
member = [0] * N
for i in range(N):
    name, score1, score2, score3 = map(str, input().split())
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    member[i] =(name, score1, score2, score3)
member.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in member:
    print(i[0])"""
    
import sys
N = int(sys.stdin.readline())
table = [list(sys.stdin.readline().split()) for _ in range(N)]
table.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in table: 
    sys.stdout.write(str(student[0]) + "\n")

