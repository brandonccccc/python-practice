x = []
y = []
ans = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(len(x)):
    if x.count(x[i]) == 1:
        ans.append(x[i])
    if y.count(y[i]) == 1:
        ans.append(y[i])
print(ans[0],end = ' ')
print(ans[1])