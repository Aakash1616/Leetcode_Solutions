class Solution:
    def solveMin(self, lst, dp, i, j, m, n):
        if i==m-1 and j==n-1:
            return lst[i][j]
        if not(0<=i<m and 0<=j<n):
            return 99999 
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j] = min(self.solveMin(lst, dp, i+1, j, m, n), self.solveMin(lst, dp, i, j+1, m, n))+lst[i][j]
        return dp[i][j]
        
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*(n) for i in range(m)]
        return self.solveMin(grid, dp, 0, 0, m, n)