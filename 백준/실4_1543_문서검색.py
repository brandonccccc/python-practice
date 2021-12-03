s = input()
find_s = input()
i = 0
cnt = 0
while i+len(find_s) <= len(s):
    if find_s in s[i:i+len(find_s)]:
        cnt += 1
        i += len(find_s)
    else: i += 1

print(cnt)