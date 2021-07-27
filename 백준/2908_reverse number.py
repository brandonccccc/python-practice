A, B = map(str, input().split())
# str로 초기화한 A와 B를 슬라이싱해서 거꾸로 가져오기 [시작 인덱스: 끝 인덱스: -1이면 거꾸로]
A = A[::-1]   # 의 뜻 : A[처음부터 : 끝까지 : 거꾸로]
B = B[::-1]

if A > B:
    print(A)
else:
    print(B)
