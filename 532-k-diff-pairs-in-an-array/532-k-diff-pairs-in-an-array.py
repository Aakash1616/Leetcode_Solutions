import itertools
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        return sum(k > 0 and i+k in c or k==0 and c[i]>1 for i in c)