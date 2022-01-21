class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum = cost_sum = st_ind = cap = 0
        for i in range(len(gas)):
            gas_sum+=gas[i]
            cost_sum+=cost[i]
            cap+=(gas[i]-cost[i])
            if cap<0:
                st_ind = i+1 
                cap = 0 
        if gas_sum<cost_sum:
            return -1 
        else:
            return st_ind
            