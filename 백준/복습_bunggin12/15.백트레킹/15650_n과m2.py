n, m = map(int, input().split())
ans = []

def back(start): # 앞 숫자가 뒷 수자보다 큰 경우를 제외하기 위해 start 변수 추가
    if len(ans) == m:  # 배열의 길이를 확인해서 길이가 됐으면
        print(" ".join(map(str, ans))) # 결과 출력. 띄어쓰기로 연결하기 위해서
        return
    for i in range(start, n+1): # 1~n까지
        if i not in ans:  # 중복 확인해서 없으면
            ans.append(i)  # 배열에 추가
            back(i+1)  # 재귀 (이전 시작한 숫자 뒤의 값부터 트레킹)
            ans.pop() # return 했을 때 이게 실행. 1, 2, 3 일때 3을 없애서 전 단계로 돌아감

back(1)