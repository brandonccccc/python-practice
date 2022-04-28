croatia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in croatia_alpha:
    s = s.replace(i, '*')
print(len(s))

#저장해 둔 크로아티아 알파벳을 1자리 문자로 치환한다.
# 순서대로 바꾸기 때문에 우선순위가 있는 경우(예로 dz=, d-)를 고려하여 list에 저장한다.
