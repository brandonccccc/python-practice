N = int(input())

def addnumber(n):
    s = str(n)
    x = 0
    for i in s:
        x += int(i)
    return x

n = input()
x = addnumber(n)
print(x)
