n, m = map(int, input().split())

def count_two(n):
    two = 0
    while n != 0:
        n //= 2
        two += n
    return two

def count_five(n):
    five = 0
    while n != 0:
        n //=5
        five += n
    return five

zero = min(count_two(n) - count_two(n - m) - count_two(m), count_five(n) - count_five(n - m) - count_five(m))
print(zero)