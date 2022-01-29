class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        st = [-1]
        mx = 0 
        for i in range(len(heights)):
            while(heights[i]<heights[st[-1]]):
                hgt = heights[st.pop()]
                w = i - st[-1] - 1 
                mx = max(mx, hgt*w)
            st.append(i)
        return mx 