class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l2 = len(s1)
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2[:len(s1)])
        cnt = 0
        for i in range(26):
            if c1[chr(i+97)]==c2[chr(i+97)]:
                cnt+=1
        for i in range(len(s2)-l2):
            if cnt==26:
                return True 
            c2[s2[i+l2]]+=1 
            if c2[s2[i+l2]]==c1[s2[i+l2]]:
                cnt+=1 
            elif c2[s2[i+l2]]==c1[s2[i+l2]]+1:
                cnt-=1 
            c2[s2[i]]-=1 
            if c2[s2[i]]==c1[s2[i]]:
                cnt+=1 
            elif c2[s2[i]]+1 == c1[s2[i]]:
                cnt-=1 
        return cnt==26