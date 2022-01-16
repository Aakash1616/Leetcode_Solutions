class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxi = 0 
        temp = 0 
        for i in seats:
            if i==0:
                temp+=1 
            else:
                temp = 0 
            maxi = max(maxi, temp)
        return max(maxi//2-(maxi%2==0)+1, max(seats.index(1), seats[::-1].index(1)))