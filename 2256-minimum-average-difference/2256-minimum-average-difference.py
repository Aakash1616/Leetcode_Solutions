class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s = sum(nums)
        mi = 9999999
        curr = 0 
        ind = 0 
        for i in range(len(nums)):
            curr+=nums[i]
            l = curr//(i+1)
            r = (s-curr)//max(len(nums)-i-1, 1)
            if mi>abs(l-r):
                mi = abs(l-r) 
                ind = i 
        return ind