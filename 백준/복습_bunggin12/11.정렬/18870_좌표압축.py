import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sorted_num = list(sorted(set(nums)))
# 딕셔너리에 정렬된 리스트 숫자를 차례로 ㅇ입력하면서 밸류값을 인덱스와 똑같이 넣는다
dic_nums = {sorted_num[i] : i for i in range(len(sorted_num))}

for i in nums:
    print(dic_nums[i], end = ' ')