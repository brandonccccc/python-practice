from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
find = list(map(int, input().split()))
cnt = 0
queue = deque([])
for i in range(1, n+1):
    queue.append(i)

for i in range(m):
    queue_index = queue.index(find[i])
    queue_len = len(queue)
    if queue_index < queue_len - queue_index:
        while True:
            if queue[0] == find[i]:
                del queue[0]
                break
            else:
                queue.append(queue.popleft())
                cnt += 1
    else:
        while True:
            if queue[0] == find[i]:
                del queue[0]
                break
            else:
                queue.appendleft(queue.pop())
                cnt+=1
print(cnt)