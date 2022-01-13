class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(lambda : -1)
        for i in range(len(nums)):
            if dic[target-nums[i]]!=-1:
                return [dic[target-nums[i]], i]
            dic[nums[i]] = i 
        