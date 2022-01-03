class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = defaultdict(lambda : -1)
        res = 0 
        for i in time:
            val = dic[(60-i%60)%60]
            if val>=0:
                res+=val 
            if dic[i%60] != -1:
                dic[i%60]+=1 
            else:
                dic[i%60] = 1 
        return res