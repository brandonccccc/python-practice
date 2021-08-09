sentence = input()
for i in range(0, len(sentence)):
    if i == 0:
        print(sentence[0], end="")
    elif i % 10 == 9:
        print(sentence[i],end = "\n")
    else:
        print(sentence[i],end = "")
