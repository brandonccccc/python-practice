import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
sign = list(map(int, input().rstrip().split()))  #+ - * //

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, mul, div):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, total * nums[depth], plus, minus, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, mul, div - 1)
        
dfs(1, nums[0], sign[0], sign[1], sign[2], sign[3])
print(maximum)
print(minimum)