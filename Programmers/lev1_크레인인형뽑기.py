def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board[i-1])):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                if len(stack) >= 2 and stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    
    return answer




print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))