#include "tools.h"
class Solution {
    public:
        int smallestIndex(vector<int>& nums) {
            int n = nums.size();
            for (int i = 0; i < n; i ++ )
            {
                if (solve(nums[i]) == i) return i;
            }
            return -1;
        }
        long long solve(int x)
        {
            long long res = 0;
            while (x)
            {
                res += x % 10;
                x /= 10;
            }
            return res;
        }
    };