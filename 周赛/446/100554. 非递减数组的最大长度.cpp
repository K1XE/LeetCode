#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        int maximumPossibleSize(vector<int>& nums) {
            vector<int> res;
            if (nums.size() == 1) return 1;
            if (nums.size() == 2)
            {
                if (nums[1] >= nums[0]) return 2;
                else return 1;
            }
            res.push_back(nums[0]);
            for (int i = 1; i < nums.size(); i ++ )
            {
                int a = nums[i];
                if (a >= res.back())
                {
                    res.push_back(a);
                }
            }
            return res.size();
        }
    };