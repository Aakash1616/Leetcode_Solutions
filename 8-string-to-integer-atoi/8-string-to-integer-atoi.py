class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s or s[:2] in "-++--":
            return 0 
        sign = -1 if (s[0] == '-') else 1 
        res = 0 
        cnt = 1 if sign==-1 else 0
        maxi = 2**31-1
        mini = -2**31
        for i in s.lstrip("+").lstrip("-"):
            if not 48<=ord(i)<=57:
                break
            temp = res*10+(ord(i)-48)
            if temp*sign<mini:
                return mini 
            elif temp*sign>maxi:
                return maxi 
            res = temp
        return sign*res