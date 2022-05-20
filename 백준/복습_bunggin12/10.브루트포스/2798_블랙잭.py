from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 카드의 모든 조합 구하기
combi_cards = list(combinations(cards, 3))
# 조합을 합으로 변환
for i in range(len(combi_cards)):
    combi_cards[i] = sum(combi_cards[i])

ans = 0
for i in combi_cards:
    # 문제의 조건 : m보다 작고 가까운 수 를 찾아 ans에 저장
    if ans < i <= m:
        ans = i
print(ans)