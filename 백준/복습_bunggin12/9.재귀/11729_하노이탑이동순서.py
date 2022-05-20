def hanoiMove(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoiMove(n-1, start, 6-start-end)
    print(start, end)
    hanoiMove(n-1, 6-start-end, end)

n = int(input())
print(2**n - 1)
hanoiMove(n, 1, 3)