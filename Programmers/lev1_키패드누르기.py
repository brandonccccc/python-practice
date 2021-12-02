def solution(numbers, hand):
    answer = ''
    l_loc = [4, 1]
    r_loc = [4, 3]
    loc = {1:[1,1], 2:[1,2], 3:[1,3], 4:[2,1], 5:[2,2], 6:[2,3], 7:[3,1], 8:[3,2], 9:[3,3], 0:[4,2]}
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l_loc = loc[i]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r_loc = loc[i]
        elif i == 2 or i == 5 or i == 8 or i == 0:
            i_loc = loc[i]
            if abs((i_loc[0] - r_loc[0])) + abs((i_loc[1] - r_loc[1])) < abs((i_loc[0] - l_loc[0])) + abs((i_loc[1] - l_loc[1])):
                answer += 'R'
                r_loc = loc[i]
            elif abs((i_loc[0] - r_loc[0])) + abs((i_loc[1] - r_loc[1])) > abs((i_loc[0] - l_loc[0])) + abs((i_loc[1] - l_loc[1])):
                answer += 'L'
                l_loc = loc[i]
            else:
                if hand == 'right':
                    answer += 'R'
                    r_loc = loc[i]
                else:
                    answer += 'L'
                    l_loc = loc[i]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))