class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dic = defaultdict(lambda : 0)
        val , mx = 0, 0 
        top_, bottom_ = [0]*6, [0]*6
        for i in range(len(tops)):
            dic[tops[i]]+=1 
            top_[tops[i]-1]+=1 
            if bottoms[i]!=tops[i]:
                dic[bottoms[i]]+=1
            bottom_[bottoms[i]-1]+=1 
            if dic[tops[i]]>mx:
                mx = dic[tops[i]]
                val = tops[i] 
            if dic[bottoms[i]]>mx: 
                mx = dic[bottoms[i]] 
                val = bottoms[i]
        if mx<len(tops):
            return -1 
        return len(tops)-max(top_[val-1], bottom_[val-1])