"""count_word = 0
count = 0
N = int(input())

for N in range(N):
    word = list(input())
    seq_word = []

    if len(word) == 1:
        count += 1
    # 바로 뒤에 연속되지 않는 문자가 나오면 seq_word에 추가
    for i in range(0,len(word)):
        if i < len(word)-1:
            if word[i] != word[i+1]:
                seq_word.append(word[i])
        else:
            seq_word.append(word[i])
        print(seq_word)
    for _ in range(1):
        for k in range(0, len(seq_word)-1):
            for l in range(k+1, len(seq_word)):
                if seq_word[k] == seq_word[l]:
                    count_word += 1
                else:
                    count_word += 0  
                print(count_word)
        if count_word == 0:
            count += 1
        count_word == 0
    
print(count)"""


case_num = int(input())
answer = []
for i in range(case_num):
    word = list(str(input()))

    for k in range(len(word)):
        if k != len(word)  and word[k] == word[k + 1]:
            pass
        elif word[k + 1:].count(word[k]) != 0:
            break
        elif k == len(word) - 1:
            answer.append(i)

print(answer)
print(len(answer))