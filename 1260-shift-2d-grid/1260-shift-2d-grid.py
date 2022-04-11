class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col, lst = len(grid[0]), sum(grid, [])  
        k = k % len(lst)  
        lst = lst[-k:] + lst[:-k] 
        return [lst[i:i+col] for i in range(0, len(lst), col)]