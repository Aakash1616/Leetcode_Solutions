class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi = float(inf), 0
        for i in prices:
            mini = min(mini, i)
            profit = i - mini
            maxi = max(maxi, profit)
        return maxi