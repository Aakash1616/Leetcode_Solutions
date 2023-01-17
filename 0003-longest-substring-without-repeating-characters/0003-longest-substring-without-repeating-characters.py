class Solution:
    def lengthOfLongestSubstring(self, s):
        st = mx = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and st <= d[s[i]]:
                st = d[s[i]] + 1
            else:
                mx = max(mx, i - st + 1)

            d[s[i]] = i

        return mx