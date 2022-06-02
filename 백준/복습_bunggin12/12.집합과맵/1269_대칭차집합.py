import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
# 집합으로 선언된 녀석들은 계산하면 집합 개념으로 알아서 계산된다.
print(len(a_set-b_set) + len(b_set - a_set))