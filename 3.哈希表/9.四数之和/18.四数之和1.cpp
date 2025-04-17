/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4) return {};
        ranges::sort(nums);
        for (int i = 0; i < nums.size() - 3; i ++ )
        {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            if (nums[i] > target && nums[i] >= 0) break;
            for (int j = i + 1; j < nums.size() - 2; j ++ )
            {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                if ((long long)nums[i] + nums[j] > target && (long long)nums[i] + nums[j] >= 0) break;
                int l = j + 1, r = nums.size() - 1;
                while (l < r)
                {
                    long long tmp = (long long) nums[i] + nums[j] + nums[l] + nums[r]; 
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

