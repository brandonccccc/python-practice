alpha = "abcdefghijklmnopqrstuvwxyz"

s = input()
for x in alpha:
    print(s.find(x), end = ' ')
    
#find 함수는 문자열에서 문자를 찾는데 사용할 수 있다.
# 문자열에 해당 문자가 없으면 -1을 출력해준다.