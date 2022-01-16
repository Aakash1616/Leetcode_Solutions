class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        lst = []
        for i in range(0,len(s),k):
            lst.append(s[i:i+k])
        lst[-1]+=((k-len(lst[-1]))*fill)
        return lst