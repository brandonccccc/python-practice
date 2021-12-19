"""n = int(input())
milk = [0, 1, 2]
cnt = 0
market = list(map(int, input().split()))
i = 0
j = 0
while i < len(market):
    if market[i] == milk[j % 3]:
        # 영희가 우유를 마시는 순서와 가게에서 파는 우유가 같으면 cnt += 1, 영희 순서, 가게 각각 +1 로 갱신
        cnt += 1
        i += 1
        j += 1
    else:
        # 영희가 마시는 순서와 가게가 다르면 가게만 +1로 갱신
        i += 1
    
print(cnt)
"""

n = int(input())
a = list(map(int, input().split())) 
count = 0 

for i in range(n): 
    if a[i] == count % 3: 
        count = count + 1 
        
print(count)

