from itertools import product
def solution(word):
    words_list = []
    for i in range(6):
        words_list += list(map(''.join, product("AEIOU", repeat=i)))
    words_list.sort()
    print(words_list)
    return words_list.index(word)

print(solution('AA'))