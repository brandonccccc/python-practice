# 앞의 문자와 같지 않을때 문자열에 추가
def word_grouping(s):
    alpha = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            alpha += s[i]
    return alpha

n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    # word_grouping 함수 돌린 문자열의 길이와 중복제거(set)한 문자열의 길이를 비교
    if len(word_grouping(s)) == len(set(word_grouping(s))):
        # 길이가 같다면 중복이 없는 것이므로 그룹단어이므로 cnt에 1 더함
        cnt += 1
    
print(cnt)