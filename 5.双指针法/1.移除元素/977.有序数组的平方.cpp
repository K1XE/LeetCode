/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size());
        int l = 0, r = nums.size() - 1, cnt = nums.size() - 1;
        while (l <= r)
        {
            int nl = nums[l] * nums[l], nr = nums[r] * nums[r];
            if (nl >= nr) res[cnt --] = nl, l ++;
            else res[cnt --] = nr, r --;
        }
        return res;
    }
};
// @lc code=end

