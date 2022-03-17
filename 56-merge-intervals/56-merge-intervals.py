class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i, l, res = 0, len(intervals), []
        while(i<l):
            mx = intervals[i][1]
            for j in range(i+1, l):
                if intervals[j][0]<=mx:
                    mx = max(mx, intervals[j][1] )
                else:
                    res.append([intervals[i][0], mx])
                    i = j 
                    break 
            else:
                res.append([intervals[i][0], mx])
                break 
        return res 