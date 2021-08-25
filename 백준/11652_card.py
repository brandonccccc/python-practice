import sys
N = int(sys.stdin.readline())
count = {}
for i in range(N):
    num = int(sys.stdin.readline())
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
# 딕셔너리를 리스트로, 키, 밸류를 튜플로 저장
count = list(zip(count.keys(), count.values()))
count.sort(key = lambda x: (-x[1], x[0]))
print(count[0][0])