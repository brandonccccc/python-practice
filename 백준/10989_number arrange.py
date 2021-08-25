import sys
N = int(sys.stdin.readline())
count = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    count[num] = count[num] + 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
            
# 입력받는 수에 제한이 있는 경우, 경우의 수마다 값을 저장해서 출력하는것이 복잡도가 더 낮다.
# sort등을 사용하는 경우 시간 복잡도는 O(log(N)) 이다.
# 리스트에 값을 저장하고 출력하는 경우 시간복잡도는 O(n)이다