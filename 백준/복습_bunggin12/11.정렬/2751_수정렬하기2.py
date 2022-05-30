# 시간 복잡도 nlogn 인 정렬
# 힙 정렬, 병합정렬 등
# 파이썬 내장 함수인 sort의 시간 복잡도도 nlogn이므로 쓸 수 있다.
# for 를 여러번 쓰다보니 input으로 입력을 받으면 시간초과가 뜸
# sys 입력으로 바꾸면 통과
import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
for i in nums:
    print(i)
    
