n = input() # 1<=n<=100,000,000
sums = [0, 9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000]
for i in range(len(sums)):
    sums[i] = sums[i] * i
length = len(n)
n = int(n)
answer = 0

answer += sum(sums[:length]) + (n+1-10**(length-1))*length

print(answer)