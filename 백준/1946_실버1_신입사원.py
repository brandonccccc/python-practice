import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h = []
    cnt = 1
    
    n = int(input())
    for _ in range(n):
        # 지원자 성적 입력
        h.append(list(map(int, input().split())))
    # 서류 등수 순서로 정렬
    h.sort()
    min = h[0][1]
    
    for i in range(1,n):
        if h[i][1] < min:
            cnt += 1
            min = h[i][1]
            
print(cnt)