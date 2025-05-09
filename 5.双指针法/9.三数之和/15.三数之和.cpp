/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); i ++ )
        {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int target = - nums[i];
            int l = i + 1, r = nums.size() - 1;
            while (l < r)
            {
                if (nums[l] + nums[r] == target)
                {
                    res.push_back({nums[i], nums[l], nums[r]});
                    while (l < r && nums[r] == nums[r - 1]) r --;
                    while (l < r && nums[l] == nums[l + 1]) l ++;
                    l ++, r --;
                }
                else if (nums[l] + nums[r] > target)
                {
                    r --;
                }
                else l ++;
            }
        }
        return res;
    }
};
// @lc code=end

