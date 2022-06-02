import sys
input = sys.stdin.readline

n, m = map(int, input().split())
monster_nums = {}
nums_monster = {}
for i in range(n):
    keyin = input().rstrip()
    monster_nums[keyin] = i + 1
    nums_monster[str(i+1)] = keyin

for i in range(m):
    search = input().rstrip()
    if search in monster_nums:
        print(monster_nums[search])
    else:
        print(nums_monster[search])