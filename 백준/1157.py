# 갯수를 세기위해서 함수 불러오기
from collections import Counter

# 입력받은 단어를 소문자로 받아서 초기화
word = input().lower()
# 알파벳 개수를 세고, 많은 순서로 나역
word_count = Counter(word).most_common()
# 딕셔너리 형태로 형변환
word_count = dict(word_count)
# 딕셔너리 형태에서 밸류값이 큰 key를 저장하는 리스트 생성 (여러개면 여러개 저장)
keys = [k for k, v in word_count.items() if max(word_count.values()) == v]

# keys 리스트가 2개 이상이면 ? 출력, 1개면 값 출력
if len(keys) > 1:
    print('?')
else:
    print(keys[0].upper())
