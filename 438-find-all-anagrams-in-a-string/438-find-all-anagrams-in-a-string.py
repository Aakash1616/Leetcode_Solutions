from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        Scounter, Pcounter = Counter(s[:l-1]), Counter(p)
        res = []
        for i in range(l-1, len(s)):
            Scounter[s[i]]+=1 
            if Scounter == Pcounter:
                res.append(i-l+1)
            Scounter[s[i-l+1]]-=1 
            if Scounter[s[i-l+1]]==0:
                del Scounter[s[i-l+1]]
        return res