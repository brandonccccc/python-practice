T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [[0]*n for _ in range(2)]
    for i in range(2):
        sticker[i] = list(map(int, input().split()))

max_num = max(map(max, sticker))



print(sticker)
print(sticker.index(max(sticker)))
max_sticker = list(map(max, sticker))
print(max_sticker)
print(max(sticker))