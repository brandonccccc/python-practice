from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0

for cards in combinations(cards, 3):
    temp_sum = sum(cards)
    if max_sum < temp_sum <= m:
        max_sum = temp_sum


print(max_sum)