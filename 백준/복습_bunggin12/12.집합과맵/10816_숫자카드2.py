import sys
input = sys.stdin.readline

n = int(input())
ncard_list = map(int, input().split())
n_cards = {}

for card in ncard_list:
    if card in n_cards:
        n_cards[card] += 1
    else:
        n_cards[card] = 1
m = int(input())
mcard_list = map(int, input().split())

for card in mcard_list:
    if card in n_cards:
        print(n_cards[card], end = ' ')
    else: print(0, end = ' ')

# 단순히 숫자의 나열로 사용할거면 굳이 리스트로 안만들고 map으로만 선언해도 됨
# 리스트는 메모리를 차지하고 입력하여 값을 넣거나 탐색하는데 시간이 많이 걸림

