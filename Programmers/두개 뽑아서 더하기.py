def solution(numbers):
    a = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j :
                a.append(numbers[i]+numbers[j])
    return sorted(list(set(a)))