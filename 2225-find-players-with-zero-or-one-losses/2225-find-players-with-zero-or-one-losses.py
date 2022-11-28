class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = collections.defaultdict(lambda : 0)
        l = collections.defaultdict(lambda : 0)
        for i in matches:
            w[i[0]]+=1 
            l[i[1]]+=1
        ans = [[], []]
        for i in w:
            if not l[i]:
                ans[0].append(i) 
        for i in l:
            if l[i]==1:
                ans[1].append(i) 
        ans[0].sort()
        ans[1].sort() 
        return ans 
        