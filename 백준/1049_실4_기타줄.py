import sys
input = sys.stdin.readline

n, m = map(int, input().split())
string_set = []
string = []
for _ in range(m):
    a, b = (map(int, input().split()))
    string_set.append(a)
    string.append(b)

if min(string_set) < min(string)*6:
    print(min(min(string_set) * ((n//6) + 1), (min(string_set) * (n//6)) + (min(string) * (n%6))))
else:
    print(n * min(string))
