class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda l: l[1])
        ans, arrow = 0, 0
        for [start, end] in points:
            if ans == 0 or start > arrow:
                ans, arrow = ans + 1, end
        return ans