/*
 * @lc app=leetcode.cn id=349 lang=cpp
 *
 * [349] 两个数组的交集
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> res, set(nums1.begin(), nums1.end());
        for (auto x : nums2)
            if (set.find(x) != set.end()) res.insert(x);
        return vector<int>(res.begin(), res.end());
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
            unordered_set<int> set1, set2;
            vector<int> res;
            for (auto x : nums1)
                set1.insert(x);
            for (auto x : nums2)
                set2.insert(x);
            for (auto x : set1)
                if (set2.find(x) != set2.end()) res.push_back(x);
            return res;
        }
    };
