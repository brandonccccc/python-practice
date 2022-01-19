class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_re = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                s_re += i.lower()
        if s_re == s_re[::-1]:
            return True
        else:
            return False
        
        
