S = input()
result = [0] * 26
for i in S:
    result[ord(i) - 97] = S.count(i)
for i in result:
    print(i, end=" ")
    
"""- input으로 문자열을 입력받습니다.
- 알파벳 a ~ z까지 총 26개이므로 lst배열에 [0]을 총 26개로 초기화 했습니다.
- ord(문자)는 문자를 숫자로 바꿔주는 함수이므로 알파벳 a의 아스키코드인 97을 빼주어 lst 배열의 index와 맞춰주었습니다.

출처: https://imksh.com/38 [강승현입니다]"""