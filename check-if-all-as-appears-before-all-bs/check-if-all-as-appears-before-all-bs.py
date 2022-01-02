class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        if 'a' not in s[s.index('b'):]:
            return True 
        return False