def solution(phone_book):
    answer = True
    dic = {}
    
    for number in phone_book:
        dic[number] = 1
    
    for number in phone_book:
        tmp = ""
        for num in number:
            tmp += num
            if tmp in dic and tmp != number:
                answer = False
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))


# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True