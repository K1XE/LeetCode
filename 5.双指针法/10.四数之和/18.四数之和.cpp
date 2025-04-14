/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        if (nums.size() < 4) return res;
        for (int i = 0; i < nums.size() - 3; i ++ )
        {
            if (nums[i] > target && nums[i] >= 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.size() - 2; j ++ )
            {
                long long tmp = nums[i] + nums[j];
                if (tmp > target && tmp >= 0) break;
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int l = j + 1, r = nums.size() - 1;
                while (l < r)
                {
                    tmp = (long long)nums[i] + nums[j] + nums[l] + nums[r];
                    if (tmp == target)
                    {
                        res.push_back({nums[i], nums[j], nums[l], nums[r]});
                        while (l < r && nums[l] == nums[l + 1]) l ++;
                        while (l < r && nums[r] == nums[r - 1]) r --;
                        l ++, r --;
                    }
                    else if (tmp > target)
                    {
                        r --;
                    }
                    else l ++;
                }
            }
        }
        return res;
    }
};
// @lc code=end

