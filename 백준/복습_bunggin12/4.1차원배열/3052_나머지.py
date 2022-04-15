nums = [int(input())%42 for _ in range(10)]
print(len(set(nums)))

#중복되는 값을 없애기 위해서 set(집합)을 사용