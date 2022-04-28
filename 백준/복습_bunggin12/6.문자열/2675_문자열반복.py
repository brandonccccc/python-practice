t = int(input())
for _ in range(t):
    r, s = map(str, input().split())
    answer = ''
    for i in range(len(s)):
        answer += s[i]*int(r)
    print(answer)
        