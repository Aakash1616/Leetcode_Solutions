class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0]) for i in range(len(grid))] 
        dp[0][0] = grid[0][0] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i and not j:
                    continue 
                elif not i:
                    dp[0][j] = grid[0][j] + dp[0][j-1] 
                elif not j:
                    dp[i][0] = grid[i][0] + dp[i-1][0]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) 
        return dp[-1][-1] 