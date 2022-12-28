class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles) 
        while(k):
            heapq.heappush(piles, -math.ceil(-heapq.heappop(piles)/2))
            k-=1 
        return -sum(piles) 
    