from collections import deque

def solution(priorities, location):
    answer = 0
    #처음 정하는 인덱스 기준으로 location이 정해지므로 인덱스와 값을 같이 저장
    s = deque([(v, i) for i, v in enumerate(priorities)])
    
    while len(s):
        # 맨 앞 항목을 일단 뺀다
        temp = s.popleft()
        # s가 빈 리스트가 아니고 맨 앞 항목보다 max값이 크면 다시 맨뒤에 넣는다.
        if s and max(s)[0] > temp[0]:
            s.append(temp)
            
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer
            

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))