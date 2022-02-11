// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

int convertFive(int n);

// Driver program to test above function
int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << convertFive(n) << endl;
    }
}// } Driver Code Ends


/*you are required to complete this method*/
int convertFive(int n) {
    int cnt = 0, val = 0;
    while(n){
        if (n%10==0){
            val+=(5*pow(10, cnt));
        }
        else{
            val+=(n%10*pow(10, cnt));
        }
        cnt+=1;
        n/=10;
    }
    return val;
}