import sys
input = sys.stdin.readline

def toggle(num):
    if s_list[num] == 0:
        s_list[num] = 1
    else:
        s_list[num] = 0
    return

s = int(input())
s_list = [-1] + list(map(int, input().split()))
t = int(input())

for _ in range(t):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, s+1, num):
            toggle(i)
    else:
        toggle(num)
        for k in range(s // 2):
            if num + k > s or num - k < 1 :
                break
            if s_list[num+k] == s_list[num-k]:
                toggle(num+k)
                toggle(num-k)
            else:
                break

for i in range(1, s+1):
    print(s_list[i], end = ' ')
    if i % 20 == 0:
        print()