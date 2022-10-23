class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        s = n*(n+1)//2 
        arr = [0]*n 
        for i in range(n):
            if arr[nums[i]-1] == 1:
                a = nums[i] 
            else:
                arr[nums[i]-1] = 1 
                s-=nums[i] 
        return [a, s] 

            