class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        col = False
        for i in range(m):
            if matrix[i][0] == 0:
                col = True
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0  
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0 
        if not matrix[0][0]:
            for i in range(n):
                matrix[0][i] = 0 
        if col:
            for i in range(m):
                matrix[i][0] = 0 
        return matrix