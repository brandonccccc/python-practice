def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        sizes[i].sort()
    for i in range(len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    return max(w) * max(h)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))