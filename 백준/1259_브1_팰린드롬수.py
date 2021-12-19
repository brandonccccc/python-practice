while True:
    n = int(input())
    if n == 0:
        break
    n_list = list(str(n))
    n_list_reverse = reversed(n_list)
    if n == int(''.join(n_list_reverse)):
        print('yes')
    else:
        print('no')
