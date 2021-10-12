def solution(n, arr1, arr2):
    answer = [[0 for _ in range(n)] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        arr1[i] = list("{0:b}".format(arr1[i]).zfill(n))
        arr2[i] = list("{0:b}".format(arr2[i]).zfill(n))
        
    for i in range(len(arr1)):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                answer[i][j] = '#'
            else:
                answer[i][j] = ' '
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
        
    return answer


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5
answer = [[0 for _ in range(n)] for _ in range(len(arr1))]
print(answer)
for i in range(len(arr1)):
    arr1[i] = list("{0:b}".format(arr1[i]).zfill(n))
    arr2[i] = list("{0:b}".format(arr2[i]).zfill(n))
    
for i in range(len(arr1)):
    for j in range(n):
        if arr1[i][j] == '1' or arr2[i][j] == '1':
            answer[i][j] = '#'
        else:
            answer[i][j] = ' '
for i in range(len(answer)):
    answer[i] = "".join(answer[i])

print(arr1)
print(arr2)
print(answer)