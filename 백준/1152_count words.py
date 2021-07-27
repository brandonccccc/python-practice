import collections
txt = input()
txt_word_list = txt.split()
# 띄어쓰기로 나눠진 단어를 카운트 (딕셔너리 형식으로 저장됨)
word_count = collections.Counter(txt_word_list)
# 딕셔너리 형식으로 저장된 값들 중 밸류만을 뽑아서 리스트로 만듦
sum_word_count = word_count.values()

# 리스트 값을 다 더해서 출력
print(sum(sum_word_count))
