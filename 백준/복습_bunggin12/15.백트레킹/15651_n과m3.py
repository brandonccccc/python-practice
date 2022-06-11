n, m = map(int, input().split())
ans = []

def back():
    if len(ans) == m:  # 배열의 길이를 확인해서 길이가 됐으면
        print(" ".join(map(str, ans))) # 결과 출력. 띄어쓰기로 연결하기 위해서
        return
    for i in range(1, n+1): # 1~n까지
        ans.append(i)  # 배열에 추가
        back()  # 재귀 
        ans.pop() # return 했을 때 이게 실행. 1, 2, 3 일때 3을 없애서 전 단계로 돌아감
back()
# 15649번 코드에서 중복 확인하는 부분 
#         if i not in ans:  # 중복 확인해서 없으면
# 을 삭제하면 중복되는 것도 전부 출력한다.