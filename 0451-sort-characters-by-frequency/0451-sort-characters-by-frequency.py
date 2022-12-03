class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        arr = [[] for _ in range(len(s)+1)]
        for c, freq in ctr.items():
            arr[freq].append(c)
        ans = []
        for freq in range(len(s), -1, -1):
            for c in arr[freq]:
                ans.append(c * freq)
        return "".join(ans)