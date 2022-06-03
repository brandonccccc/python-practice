import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(6)]

max_width, max_height = 0, 0
max_width_idx, max_height_idx = 0, 0
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[i][1] > max_width:
            max_width = arr[i][1]
            max_width_idx = i
    else:
        if arr[i][1] > max_height:
            max_height = arr[i][1]
            max_height_idx = i
min_width = abs(arr[(max_width_idx-1) % 6][1] - arr[(max_width_idx+1) % 6][1])
min_height = abs(arr[(max_height_idx-1) % 6][1] - arr[(max_height_idx+1) % 6][1])
print(((max_height*max_width) - (min_height * min_width)) * n)

# 가장 긴 변의 양변의 차 가 작은 사각형의 높이, 너비가 된다.
