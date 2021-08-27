def solution(s):
    ndic = ["0", "zero", "1", "one", "2", "two", "3", "three",
    "4", "four", "5", "five", "6", "six", "7", "seven", "8", "eight", "9", "nine"]
    answer = s
    for i in range(1, 20, 2):
        answer = answer.replace(ndic[i], ndic[i-1])
    answer = int(answer)
    return answer