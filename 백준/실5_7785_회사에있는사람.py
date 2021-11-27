import sys
input = sys.stdin.readline
n = int(input())
pe = {}

for _ in range(n):
  p, c = input().split()

  if c == 'enter':
    pe[p] = 'enter'
  else:
    if pe[p]:
      del pe[p]

for people in sorted(pe, reverse=True):
  print(people)