class Solution:
    def bitwiseComplement(self, n: int) -> int:
        val = 2 
        while val<=n:
            val*=2 
        return val-1-n