class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN, i = 0, j = 0, tmp = 0 ; 
        while(i<nums.size()){
            tmp+=nums[i];
            res = max(res, tmp); 
            if (tmp<0) {
                tmp = 0;
                j = i ;
            }
            i+=1; 
        }
        return res; 
    }
};