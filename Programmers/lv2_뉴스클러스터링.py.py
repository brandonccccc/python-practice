def solution(str1, str2):
    s1 = []
    s2 = []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha() == True:
            s1.append(str1[i:i+2].upper())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha() == True:
            s2.append(str2[i:i+2].upper())

    intersection = 0
    union = 0

    for s in set(s1 + s2):
        union += max(s1.count(s), s2.count(s))
        intersection += min(s1.count(s), s2.count(s))

    if union == 0:
        return 65536
    return int(intersection / union * 65536)


# def sum_list(list1, list2):
#     temp1 = list1.copy()
#     temp2 = list1.copy()
#     for i in list2:
#         if i not in temp1:
#             temp2.append(i)
#         else:
#             temp1.remove(i)
#     return temp2

# def cross_list(list1, list2):
#     result = []
#     for i in list2:
#         if i in list1:
#             list1.remove(i)
#             result.append(i)
#     return result

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))

