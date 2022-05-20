# 체스판 전체와 시작점을 변수로 W/B 판별하는 함수
def check_space(board, x, y):
    cnt_w = 0
    cnt_b = 0
    for k in range(x, x+8):
        for l in range(y, y+8):
            if (k+l)%2 == 0:
                if board[k][l] != 'W':
                    cnt_w += 1
                if board[k][l] != 'B':
                    cnt_b += 1
            else:
                if board[k][l] != 'B':
                    cnt_w += 1
                if board[k][l] != 'W':
                    cnt_b += 1
    return min(cnt_w, cnt_b)

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
# 각 시작 포인트 기준으로 칠해야할 칸 갯수 저장할 리스트 초기화
cnt_list = []

for i in range(n-7):
    for j in range(m-7):
        cnt_list.append(check_space(board, i, j))
                
print(min(cnt_list))