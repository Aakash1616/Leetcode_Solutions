class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        d = collections.defaultdict(lambda : [])
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0]) 
        q = collections.deque([source])  
        t = [0]*n 
        t[source] = 1 
        while(q):
            ele = q.popleft()  
            if ele==dest:
                return True 
            for i in d[ele]:
                if t[i]==0:
                    t[i] = 1
                    q.append(i) 
        return False 