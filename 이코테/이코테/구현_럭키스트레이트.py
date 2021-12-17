n = int(input()) # 10 <= n <= 99,999,999
n_list = list(str(n))
n_list = list(map(int, n_list))
middle = len(n_list) // 2

if sum(n_list[:middle]) == sum(n_list[middle:]):
    print('LUCKY')
else:
    print('READY')
