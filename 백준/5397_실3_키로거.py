t = int(input())
for _ in range(t):
    left, right = [], []
    L = list(input())
    for i in L:
        if i == '<':
            if left:
               right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop()) 
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left) + ''.join(reversed(right)))