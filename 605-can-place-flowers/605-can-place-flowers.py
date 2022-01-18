class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0 
        temp = 0 
        lst = [0]+flowerbed+[0]
        for i in lst:
            if i==1:
                if temp>=3:
                    res+=(temp-(temp%2==0))//2
                temp = 0 
            else:
                temp+=1 
            if res>=n:
                return True 
        return res+((temp-(temp%2==0))//2)>=n