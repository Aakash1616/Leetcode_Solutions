class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0 
        c = collections.Counter(tasks)
        for i in c:
            if c[i]==1: return -1 
            elif c[i]%3==0: res+=c[i]//3 
            else: res+=c[i]//3+1   
        return res