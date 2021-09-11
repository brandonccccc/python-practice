import sys
S1 = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline())
S2 = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'D':
        if S2:
            S1.append(S2.pop())
        else:
            continue
    elif command[0] == 'L':
        if S1:
            S2.append(S1.pop())
        else:
            continue
    elif command[0] == 'B':
        if S1:
            S1.pop()
        else:
            continue
    elif command[0] == 'P':
        S1.append(command[1])

print(''.join(S1 + list(reversed(S2))))

"""시간 복잡도 inset나 del은 O(n)이고
append랑 pop이 O(1) 이다."""