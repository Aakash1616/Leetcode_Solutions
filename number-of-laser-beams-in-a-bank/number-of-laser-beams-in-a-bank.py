class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt = 0 
        l = len(bank)
        i = 0 
        while(i<l-1):
            one = bank[i].count('1')
            if one>=1:
                for j in range(i+1, l):
                    ones = bank[j].count('1')
                    if ones>=1:
                        cnt+=(one*ones)
                        i = j 
                        one = ones 
                        break 
                else:
                    i+=1 
            else:
                i+=1 
        return cnt