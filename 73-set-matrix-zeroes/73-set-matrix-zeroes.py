class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for l in range(n):
                        if matrix[i][l]!=0:
                            matrix[i][l] = -314 
                    for k in range(m):
                        if matrix[k][j]!=0:
                            matrix[k][j] = -314
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-314:
                    matrix[i][j] = 0 
        return matrix