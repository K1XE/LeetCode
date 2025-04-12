/*
 * @lc app=leetcode.cn id=1863 lang=cpp
 *
 * [1863] 找出所有子集的异或总和再求和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
    public:
        int subsetXORSum(vector<int>& nums) {
            dfs(nums, 0, 0);
            return ans;
        }
    private:
        int ans = 0;
        void dfs(vector<int>& nums, int idx, int cur)
        {
            if (idx == nums.size())
            {
                ans += cur;
                return;
            }
            dfs(nums, idx + 1, cur ^ nums[idx]);
            dfs(nums, idx + 1, cur);
        }
    };
// @lc code=end

