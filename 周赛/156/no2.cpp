#include "tools.h"
using namespace std;

class Solution {
    public:
        int minOperations(vector<int>& nums) {
            int n = nums.size();
            int i = 0;
            int res = 0;
            stack<int> stk;
            for (; i < n; i ++ )
            {
                while (stk.size() && stk.top() > nums[i])
                {
                    stk.pop();
                }
                if (nums[i] > 0)
                {
                    if (!stk.size() || stk.top() < nums[i])
                    {
                        res ++;
                        stk.emplace(nums[i]);
                    }
                }
            }
            return res;
        }
    };