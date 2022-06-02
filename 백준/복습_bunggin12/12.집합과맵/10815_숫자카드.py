import sys
input = sys.stdin.readline

n = int(input())
n_cards = list(map(int, input().split()))
m = int(input())
m_cards = list(map(int, input().split()))
dic_cards = {}

for i in m_cards:
    if i in dic_cards:
        dic_cards[i] += 1
    else: dic_cards[i] = 0
for i in n_cards:
    if i in dic_cards:
        dic_cards[i] += 1
    else: dic_cards[i] = 0
for i in m_cards:
    print(dic_cards[i], end = ' ')
    
#다른 사람 풀이 : 이진탐색
# set을 쓰긴 하는데 그냥 n_cards 만 set으로 만들고 for로 돌림
