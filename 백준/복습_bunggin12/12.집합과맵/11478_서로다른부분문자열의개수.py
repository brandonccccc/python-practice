import sys
input = sys.stdin.readline

s = str(input().rstrip())
s_set = set()
# 이중 for문으로 돌면서 모든 연속된 경우에 대해서 s_set에 추가한다.
for i in range(len(s)):
    for j in range(i, len(s)):
        # 집합으로 선언된 곳에 추가하기 때문에 중복된 건 알아서 없어진다.
        s_set.add(s[i:j+1])
print(len(s_set))