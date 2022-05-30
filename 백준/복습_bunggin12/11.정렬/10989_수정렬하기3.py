# 계수(카운팅) 정렬 이용
# 리스트로 작성하게되면 메모리가 과하게 사용되어 메모리 초과가 뜬다.
# 딕셔너리를 이용해서 리스트를 여러개 생성하지 않도록 한다
# 그럼에도 메모리가 부족.
# 메모리 제한이 극한이다 8MB
# 따라서 일반적인 정렬 방식을 사용하면 왠만하면 시간초과/메모리초과 가 나온다.
# 입력되는 수의 크기는 10000 까지 이므로 10001칸의 리스트를 만들고
# 인덱스에 해당하는 값이 들어오면 1씩 더한다.
# 0 이 아닌 인덱스에 대하여 입력된 횟수만큼을 출력해내면 
# 별도의 정렬 알고리즘 없이 정렬된 값을 출력할 수 있다.
import sys
input = sys.stdin.readline

"""n = int(input())
arr = [int(input()) for _ in range(n)]

count_dict = {}
for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
    
result = []

for num in range(max(arr) + 1):
    while num in count_dict and count_dict[num] != 0:
        result.append(num)
        count_dict[num] -= 1

for i in result:
    print(i)
"""

n = int(input())
count = [0] * 10001
for i in range(n):
    num = int(input())
    count[num] += 1
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)