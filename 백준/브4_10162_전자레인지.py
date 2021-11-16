T = int(input())
times = [300, 60, 10]
answer = [0, 0, 0]
for i in range(len(times)):
    answer[i] += T // times[i]
    T = T % times[i]

if T == 0:
    for time in answer:
        print(time, end = ' ')
else:
    print(-1)