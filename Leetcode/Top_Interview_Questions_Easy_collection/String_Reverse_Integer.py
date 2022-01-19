class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        if x[0] == '-':
            x = '-' + ''.join(list(reversed(x[1:])))
        else:
            x = ''.join(list(reversed(x)))
        if (-1)*2**31 <= int(x) <= 2**31 -1:
            return int(x)
        else:
            return 0
        
    
print(Solution().reverse(-123))