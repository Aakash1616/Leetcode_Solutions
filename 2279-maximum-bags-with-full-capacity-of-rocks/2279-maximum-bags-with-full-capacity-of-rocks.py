class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        tmp = [[capacity[i]-rocks[i], i] for i in range(len(rocks))] 
        tmp.sort(key = lambda k : k[0]) 
        res = 0 
        for i in tmp:
            ind = i[1] 
            if capacity[ind]-rocks[ind]<=additionalRocks:
                additionalRocks -= capacity[ind]-rocks[ind] 
                res+=1 
            else:
                break 
        return res 