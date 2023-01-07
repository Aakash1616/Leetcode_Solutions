class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, ttl, curr, start = len(gas), 0, 0, 0
        
        for i in range(n):
            ttl += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                start = i + 1
        return -1 if (ttl < 0) else start