from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        temp = prices.popleft()
        sec = 0
        for q in prices:
            sec += 1
            if temp > q:
                break
        answer.append(sec)
    return answer

print(solution([1,2,3,2,3]))