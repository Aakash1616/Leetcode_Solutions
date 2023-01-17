class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = tmp = 0
        for i in s:
            if i=="1":
                tmp+=1 
            else:
                res = min(res+1, tmp)
        return res 