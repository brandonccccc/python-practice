def one_check(n):
    one = '1'
    while True:
            if int(one) % n == 0:
                answer = len(one)
                break
            one += '1'
    return answer
        
while True:
    try:
        n = int(input())
        print(one_check(n))
    except EOFError:
        break