d = []
for _ in range(5):
    d.append(int(input()))
min_price = min(d[0]+d[3], d[0]+d[4], d[1]+d[3], d[1]+d[4],d[2]+d[3], d[2]+d[4])

print(min_price - 50)