/*
 * @lc app=leetcode.cn id=238 lang=cpp
 *
 * [238] 除自身以外数组的乘积
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> suf(nums.size());
        int pre = nums[0];
        suf[nums.size() - 1] = nums[nums.size() - 1];
        for (int i = nums.size() - 2; i > 0; i -- )
        {
            suf[i] = suf[i + 1] * nums[i];
        }
        suf[0] = suf[1];
        for (int i = 1; i < nums.size() - 1; i ++ )
        {
            suf[i] = pre * suf[i + 1];
            pre *= nums[i];
        }
        suf[nums.size() - 1] = pre;
        return suf;
    }
};
// @lc code=end

class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            vector<int> pre(nums.size()), suf(nums.size());
            vector<int> res(nums.size());
            pre[0] = nums[0], suf[nums.size() - 1] = nums[nums.size() - 1];
            for (int i = 1; i < nums.size(); i ++ )
            {
                pre[i] = pre[i - 1] * nums[i];
            }
            for (int i = nums.size() - 2; i >= 0; i -- )
            {
                suf[i] = suf[i + 1] * nums[i];
            }
            res[0] = suf[1], res[nums.size() - 1] = pre[nums.size() - 2];
            for (int i = 1; i < nums.size() - 1; i ++ )
            {
                res[i] = pre[i - 1] * suf[i + 1];
            }
            return res;
        }
    };