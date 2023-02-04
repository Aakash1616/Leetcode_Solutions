class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr = Counter(s1)
        tmp = 0 
        for i, v in enumerate(s2):
            ctr[v]-=1 
            while(ctr[v]<0):
                ctr[s2[tmp]]+=1 
                tmp+=1 
            if i-tmp+1==len(s1):
                return True 
        return False 