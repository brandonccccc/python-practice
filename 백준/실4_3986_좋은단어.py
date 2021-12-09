n = int(input())
answer = 0
for _ in range(n):
    stack = []
    s = input()
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        answer += 1

print(answer)