class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0 
        while( target > 1 ):
            if maxDoubles==0:
                return res+(target-1)
            if target % 2 == 0:
                target = target>>1 
                maxDoubles-=1 
            else:
                target-=1 
            res+=1
        return res