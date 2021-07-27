word = input().upper()
dial = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9}
word_list = []

for i in range(len(word)):
    # 다이얼 딕셔터리 키에 있으면 그 키에 해당하는 밸류 +1을 리스트에 저장
    if word[i] in dial.keys():
        word_list.append(dial[word[i]]+1)

print(sum(word_list))