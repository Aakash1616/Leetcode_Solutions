class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        while((n-1)*26>=k):
            res+="a"
            n-=1 
            k-=1 
        if k<=26:
            return res+chr(k+96) 
        return res+chr(k-(n-1)*26+96)+(n-1)*"z" 
        
        