class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0 : -1}
        mx = cnt = 0 
        for i, j in enumerate(nums):
            if j == 1:
                cnt+=1 
            else:
                cnt-=1 
            if cnt in dic:
                mx = max(mx, i - dic[cnt])
            else:
                dic[cnt] = i 
        return mx