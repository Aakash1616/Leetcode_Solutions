class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def solve(ind = 0 ):
            if ind>=len(questions): return 0
            return max(questions[ind][0]+solve(questions[ind][1]+ind+1), solve(ind+1))
        return solve()