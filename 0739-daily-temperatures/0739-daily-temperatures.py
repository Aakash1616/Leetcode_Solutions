class Solution:
    def dailyTemperatures(self, tempratures):
        ans = [0] * len(tempratures)
        st = []
        for i, t in enumerate(tempratures):
          while(st and tempratures[st[-1]] < t):
            cur = st.pop()
            ans[cur] = i - cur
          st.append(i)

        return ans