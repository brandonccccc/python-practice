def solution(clothes):
    dic = {}
    answer = len(clothes)
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    
    answer = 1
    for i in dic.values():
        answer *= (i + 1)
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))