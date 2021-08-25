def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)
    count = len(set(lottos)&set(win_nums))
    answer[0], answer[1] = rank[count+zero_count], rank[count]

    return answer
