def check_hansoo(num):
    num_list = list(map(int, str(num)))
    if len(num_list) > 1:
        d0 = num_list[0] - num_list[1]
        for i in range(1, len(num_list)):
            if d0 != (num_list[i-1] - num_list[i]):
                break
        else: return num
    
hansoo_list = []
n = int(input())
for i in range(1, n+1):
    if i < 10:
        hansoo_list.append(i)
    if check_hansoo(i) != None:
        hansoo_list.append(check_hansoo(i))
    
print(hansoo_list)
print(len(hansoo_list))