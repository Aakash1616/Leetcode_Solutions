class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {ch : i for i, ch in enumerate(s)}
        prev = curr = 0 
        res = []
        for i, x in enumerate(s):
            curr = max(curr, dic[x])
            if curr==i:
                res.append(i-prev+1)
                prev = i+1  
        return res 