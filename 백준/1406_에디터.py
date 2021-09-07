import sys
S = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline())
cs = len(S)
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'D':
        if cs == len(S):
            cs = cs
        else:
            cs += 1
    if command[0] == 'L':
        if cs == 0:
            cs = cs
        else:
            cs -= 1
    if command[0] == 'B':
        if cs == 0:
            pass
        else:
            del S[cs-1]
            cs -= 1
    if command[0] == 'P':
        S.insert(cs, command[1])
        cs += 1

S = ''.join(S) 
sys.stdout.write(S)