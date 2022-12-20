class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = collections.deque(rooms[0]) 
        vis = [0]*len(rooms) 
        vis[0] = 1 
        while(q):
            ele = q.popleft() 
            vis[ele] = 1 
            for i in rooms[ele]:
                if not vis[i]:
                    q.append(i) 
        return all(vis)