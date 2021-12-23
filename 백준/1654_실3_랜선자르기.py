k, n = map(int, input().split()) 
# 1<= k <= 10,000  1<= n <= 1,000,000  k<=n
cable = []
for _ in range(k):
    cable.append(int(input()))

start = 1
end = max(cable)
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in cable:
        total += x // mid
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
