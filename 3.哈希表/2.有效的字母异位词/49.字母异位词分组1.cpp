/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> hash;
        for (auto s : strs)
        {
            string s_sorted = s;
            sort(s_sorted.begin(), s_sorted.end());
            hash[s_sorted].push_back(s);
        }
        for (auto [key, val] : hash)
        {
            res.push_back(val);
        }
        return res;
    }
};
// @lc code=end

