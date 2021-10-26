T = int(input())
ans = []
for i in range(T):
    a, b, c = map(int, input().split())
    if a == b == c:
        ans.append(10000 + a*1000)
    elif a == b != c: ans.append(1000 + a*100)
    elif a == c != b: ans.append(1000 + a*100)
    elif b == c != a: ans.append(1000 + b*100)
    elif a != b!= c:
        ans.append(max(a, b, c) * 100)
print(max(ans))