class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0 
        l = 0
        for i in word:
            l+=1
            if i.isupper():
                cnt+=1
        return cnt==0 or (cnt==1 and word[0].isupper()) or cnt==l