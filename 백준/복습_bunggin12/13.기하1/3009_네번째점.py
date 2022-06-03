x_list = []
y_list = []
# 3개의 점이 주어지면 x, y가 두번씩 반복되기때문에 반복되지 않은 x, y를 찾으면 된다.
for _ in range(3):
    x, y = map(int, input().split())
    if x not in x_list:
        x_list.append(x)
    else: x_list.remove(x)
    if y not in y_list:
        y_list.append(y)
    else: y_list.remove(y)
print(*x_list, *y_list)