import sys
input = sys.stdin.readline

from itertools import product

n, m = map(int, input().split())

n_list = [i for i in range(1, n+1)]
n_list = [n_list] * m
n_permu = list(product(*n_list))
for i in range(len(n_permu)):
    for j in range(len(n_permu[i])):
        print(n_permu[i][j], end = ' ')
    print()
