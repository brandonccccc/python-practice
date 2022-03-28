def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        # 선행스킬을 리스트로 만들어 초기화
        skill_list = list(skill)
        #스킬트리에서의 값이 선행스킬에 있고 첫번째에 있다면 pop하고 넘어감
        for s in tree:
            if s in skill:
                # 스킬트리 값이 선행스킬에 있지만 첫번째가 아니라면 break
                if s != skill_list.pop(0):
                    break
        # for가 다 돌때까지 break 걸리지 않았다면 answer + 1 , 
        # 이 경우 skill list가 비워지지 않았더라도 for문을 돌리면서 break 되지 않았으므로 answer에 +1이 됨
        else:
            answer += 1
    return answer


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))