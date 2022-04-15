nums = []
for i in range(9):
    nums.append(int(input()))

# enumerate : index, value 나오는 함수. 리스트에 저장하던가, 그대로 쓰던가
for i, v in enumerate(nums):
    if v == max(nums): print(v, i+1)