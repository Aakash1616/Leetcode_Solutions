// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
  public:
    int thirdLargest(int a[], int n)
    {
        int f = 0, s = 0, t = 0;
        if (n<3)
            return -1;
        for(int i=0; i< n ; i++){
            if (a[i]>t){
                f = s;
                s = t;
                t = a[i];
            }
            else if (a[i]>s){
                f = s;
                s = a[i];
            }
            else if (a[i]>f){
                f = a[i];
            }
        }
        return f;
        
    }

};

// { Driver Code Starts.
 
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
	    int n;
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n;i++)
	        cin>>a[i];
	   Solution obj;
	    cout<<obj.thirdLargest(a,n)<<endl;
    }
}     // } Driver Code Ends