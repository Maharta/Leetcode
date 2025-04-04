class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        
        while (l < r):
            while self.isAlphaNum(s[l]) == False and l < len(s) - 1:
                l += 1
            while self.isAlphaNum(s[r]) == False and r > -1:
                r -= 1
            
            if (s[l].lower() != s[r].lower()):
                return False
            
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum(self, s: str) -> bool:
        return ('A' <= s <= 'Z' or
                'a' <= s <= 'z' or 
                '0' <= s <= '9')
    