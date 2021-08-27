def solution(array, commands):
    n = []
    answer = []
    for i in range(len(commands)):
        a = commands[i][0] - 1
        b = commands[i][1]
        c = commands[i][2]
        n = array[a:b]
        n.sort()
        answer.append(n[c-1])
    return answer


"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))"""