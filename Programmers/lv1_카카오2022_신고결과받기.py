def solution(id_list, report, k):
    answer = []
    id_dict = {}
    reported = {}
    for i in id_list:
        id_dict[i] = []
        reported[i] = 0
    
    report_set = list(set(report))
    for i in report_set:
        a, b = i.split()
        id_dict[a].append(b)
        reported[b] += 1
    
    for key in id_dict:
        temp = 0
        for value in id_dict[key]:
            if reported[value] >= k:
                temp += 1
        answer.append(temp)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
