n = int(input())
words = {}
for i in range(n):
    word = input()
    words[word] = len(word)
   
words = dict(sorted(words.items(), key =lambda x:x[0]))
words = sorted(words.items(), key =lambda x:x[1])

for word in words:
    print(word[0])