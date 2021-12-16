import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

n_list = [i for i in range(1, n+1)]
n_permu = list(combinations(n_list, m))
n_permu = list(map(list, n_permu))
for i in range(len(n_permu)):
    for j in range(len(n_permu[i])):
        print(n_permu[i][j], end = ' ')
    print()