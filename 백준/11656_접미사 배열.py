S = input()
S_list = [0] * len(S)

for i in range(len(S)):
    S_list[i] = S[i:]

S_list.sort()

for i in range(len(S_list)):
    print(S_list[i],end = '\n')
    