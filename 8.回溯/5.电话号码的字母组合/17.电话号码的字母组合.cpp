/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> hash;
        hash['2'] = "abc";
        hash['3'] = "def";
        hash['4'] = "ghi";
        hash['5'] = "jkl";
        hash['6'] = "mno";
        hash['7'] = "pqrs";
        hash['8'] = "tuv";
        hash['9'] = "wxyz";
        vector<string> res;
        string pack;
        if (digits.size() == 0) return res;
        dfs(0, digits, res, pack, hash);
        return res;
    }
    void dfs(int sta, string d, vector<string>& res, string& pack, unordered_map<char, string>& hash)
    {
        if (sta == d.size())
        {
            res.emplace_back(pack);
            return;
        }
        for (int i = 0; i < hash[d[sta]].size(); i ++ )
        {
            pack += hash[d[sta]][i];
            dfs(sta + 1, d, res, pack, hash);
            pack.pop_back();
        }
    }
};
// @lc code=end

