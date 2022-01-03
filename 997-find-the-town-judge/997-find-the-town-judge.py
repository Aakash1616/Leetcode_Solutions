#time complexity : O(n)
#space complexity: O(n)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        lst = [0] * (n+1)
        for i in trust:
            lst[i[0]]-=1 
            lst[i[1]]+=1 
            
        for i in range(1, n+1):
            if lst[i]==n-1:
                return i 
        return -1