class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            tmp = [1]
            for j in range(1, i+1):
                tmp.append(res[-1][j]+res[-1][j-1])
            res.append(tmp+[1])
        return res
                