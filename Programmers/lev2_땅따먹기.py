def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i-1][:j] + land[i-1][j + 1:]) + land[i][j]
            """1. 두번째 리스트 부터 처리하기 시작하면 range 문제를 해결할 수 있다.
               2. 특정 인덱스를 제외한 리스트로 부터 max 값을 받아오는 방법을 위와 같이 사용 할 수 있다.
               """
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
