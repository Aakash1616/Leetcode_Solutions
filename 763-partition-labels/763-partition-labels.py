class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = collections.Counter(s) 
        lst, res = [] , []
        prev = -1
        curr = 0 
        for i in range(len(s)):
            if s[i] not in lst:
                lst.append(s[i])
                curr+=1 
            cnt[s[i]]-=1 
            if cnt[s[i]]==0:
                curr-=1 
            if curr==0:
                res.append(i-prev)
                prev = i
                lst = [] 
        return res 
    