

class Solution:
    def minDist(self, arr, n, x, y):
        two = one = -99999999
        mini = 999999999
        for i in range(n):
            if arr[i]==y:
                mini = min(mini, i-one)
                two = i 
            elif arr[i]==x:
                mini = min(mini, i-two)
                one = i
        if mini>=9999999:
            return -1 
        return mini
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends