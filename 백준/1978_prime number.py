T = int(input())
num =[]
for _ in range(T):
    a = int(input())
    if a != 1 and a % 2 != 0 and a%3 != 0 and a%5 !=0 and a%7 != 0:
        num.append(a)
print(len(num))

