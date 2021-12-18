from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
nums = [i for i in range(n)]
teams = []

#조합으로 가능한 팀 생성 (하나의 팀이 결정되면 상대 팀은 그 반대편 인덱스이다.))
for i in list(combinations(nums, n//2)):
    teams.append(i)


min_stat_diff = 1000
for i in range(len(teams)//2):
    #A팀
    team = teams[i]
    stat_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_A += s[member][k]
    #B팀 
    team = teams[-i-1]
    stat_B = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_B += s[member][k]
    
    min_stat_diff = min(min_stat_diff, abs(stat_A - stat_B))

print(min_stat_diff)