def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]for i in range(len(arr1))]

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))


'''def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A'''