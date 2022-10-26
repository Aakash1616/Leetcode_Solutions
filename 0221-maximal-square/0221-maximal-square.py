class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mx = 0 
        r, c = len(matrix), len(matrix[0]) 
        dp = [[0]*(c+1) for i in range(r+1)] 
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i-1][j-1]=='1' else 0  
                mx = max(mx, dp[i][j])
            
        return mx**2 