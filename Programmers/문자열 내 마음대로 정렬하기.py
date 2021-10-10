def solution(strings, n):
    return sorted(sorted(strings), key = lambda x: (x[n],x))
strings = ["sun", "bed", "car"]
print(solution(strings,1))

#lambda의 효율적인 사용? Stack overflow?
