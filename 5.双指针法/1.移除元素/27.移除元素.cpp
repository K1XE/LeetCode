/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = 0, r = nums.size() - 1;
        while (l <= r)
        {
            if (nums[l] == val) swap(nums[l], nums[r --]);
            else l ++;
        }
        return r + 1;
    }
};
// @lc code=end

