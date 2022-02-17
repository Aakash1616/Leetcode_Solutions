class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.solve( candidates, target, [],  res)
        return res
    def solve(self, c, t, lst, res):
        if t<0:
            return lst
        if t==0:
            res.append(lst)
            return 
        for i in range(len(c)):
            self.solve(c[i:], t-c[i], lst+[c[i]] , res)
        