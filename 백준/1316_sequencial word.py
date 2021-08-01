count_word = 0
count = 0
#N = int(input())
word = list(input())
seq_word = []

for i in range(0, len(word)):
    if i < int(len(word)):
        if word[i] != word[i+1]:
            seq_word.append(word[i])
    else:
        seq_word.append(word[i])

print(seq_word)
