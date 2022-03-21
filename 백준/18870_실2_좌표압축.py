n = int(input())
list1 = list(map(int, input().split()))
sorted_list1 = list(sorted(set(list1)))

dic = {sorted_list1[i] : i for i in range(len(sorted_list1))}
for i in list1:
    print(dic[i], end=' ')
