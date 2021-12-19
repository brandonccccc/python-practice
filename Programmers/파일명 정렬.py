def solution(files):
    answer = []
    for i in files:
        head, number, tail = '', '', ''
        num_check = False

        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]
                num_check = True
            elif not num_check:
                head += i[j]
            else:
                tail = i[j:]
                break
        answer.append((head, number, tail))
    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))

    return [''.join(t) for t in answer]




print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

