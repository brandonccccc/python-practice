n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
    
for i in range(1, len(array)):
    for j in range(i, 0, -1): #i에서 1까지 1씩 줄이면서
        if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in range(len(array)):
    print(array[i])