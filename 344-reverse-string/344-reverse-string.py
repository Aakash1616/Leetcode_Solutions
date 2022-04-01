class Solution:
    def reve(self,s,ind,lens):
        if(ind==lens//2):
            return s
        s[lens-ind-1] ,s[ind] = s[ind],s[lens-ind-1]
        return self.reve(s,ind+1,lens)
    def reverseString(self, s: List[str]) -> None:
        return self.reve(s,0,len(s))
    