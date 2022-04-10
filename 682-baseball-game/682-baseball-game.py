class Solution:
    def calPoints(self, ops: List[str]) -> int:
        lst = [] 
        for i in ops:
            if i == "+":
                lst.append(lst[-1]+lst[-2]) 
            elif i == "D": 
                lst.append(lst[-1]*2)
            elif i == "C":
                lst.pop() 
            else:
                lst.append(int(i)) 
        return sum(lst) 