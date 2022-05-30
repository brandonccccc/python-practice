# 시간복잡도가 O(n^2)인 정렬 알고리즘 사용 (2중 for문)
# ex) 삽입 정렬, 버블 정렬
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
# 버블 정렬
for i in range(n):
    for j in range(i+1, n):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

for i in num_list:
    print(i)