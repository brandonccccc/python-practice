import sys
input = sys.stdin.readline
i = 0
while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break
    i += 1
    answer = (v // p) * l
    answer += min(v%p, l)

    print("Case {}: {}".format(i, answer))