import sys
input = sys.stdin.readline

n = int(input())

ans = 0
row = [0] * n
# 1차원 배열 사용 아이디어 : "row[i] = j"  i,j 위치에 퀸을 놓겠다.
def isPromising(x):
    for i in range(x):
        # 퀸을 놓을 수 없는 경우 
        # 1. 같은 열에 퀸이 있는 경우
        # 2. 왼쪽 대각, 오른쪽 대각에 퀸이 있는 경우
        # 위쪽부터 퀸을 채우고 있으므로 현재 i보다 큰 값들은 볼 필요가 없다.
        # 대각선 좌표를 일반화 한다.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def nQueens(x):
    global ans
    # 모든 퀸을 놓았다면 경우의수를 +1 하고 종료
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            # 현재 퀸을 놓으려는 위치가 promising 하면 다음 차례를 호출
            if isPromising(x):
                nQueens(x+1)

nQueens(0)
print(ans)