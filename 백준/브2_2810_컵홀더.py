n = int(input())
seat = str(input())
a = seat.count('S')
b = seat.count('LL')


print(min(a+b+1, len(seat)))