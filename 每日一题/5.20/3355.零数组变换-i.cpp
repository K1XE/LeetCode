/*
 * @lc app=leetcode.cn id=3355 lang=cpp
 *
 * [3355] 零数组变换 I
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> cover(n, 0);
        for (int i = 0; i < queries.size(); i ++ )
        {
            cover[queries[i][0]] --;
            if (queries[i][1] + 1 < n) cover[queries[i][1] + 1] ++;
        }
        for (int i = 1; i < n; i ++ )
        {
            cover[i] += cover[i - 1];
        }
        for (int i = 0; i < n; i ++ )
        {
            if (nums[i] + cover[i] > 0) return 0;
        }
        return 1;
    }
};
// @lc code=end

