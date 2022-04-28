s = list(input().split(' ')) # 입력되는 문장을 띄어쓰기(' ') 기준으로 나눠서 리스트에 저장
answer = []
for i in range(len(s)):
    #띄어쓰기로 끝나거나 시작하는 경우 리스트에 '' 가 들어있으므로 아닌 경우에만 answer로 옮김
    if s[i] != '':
        answer.append(s[i])

print(len(answer))