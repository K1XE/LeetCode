/*
 * @lc app=leetcode.cn id=350 lang=cpp
 *
 * [350] 两个数组的交集 II
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        array<int, 1005> hash1{};
        vector<int> res;
        for (auto x : nums1)
        {
            hash1[x] ++;
        }
        for (auto x : nums2)
        {
            if (hash1[x] > 0)
            {
                res.push_back(x);
                -- hash1[x];
            }
        }
        return res;
    }
};
// @lc code=end

