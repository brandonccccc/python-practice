import sys
input = sys.stdin.readline

s = input().rstrip()
s_list = list(map(str, s))
answer = []
print(s_list)
start = 0

for i in range(len(s_list)):
    if s_list[i] == '<':
        start = i
    if s_list[i] == '>':
        answer.append(''.join(s_list[start:i+1]))
        start = i+1

print(answer)