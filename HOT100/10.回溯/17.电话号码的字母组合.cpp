/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> hash;
        hash['2'] = "abc", hash['3'] = "def", hash['4'] = "ghi",
        hash['5'] = "jkl", hash['6'] = "mno", hash['7'] = "pqrs",
        hash['8'] = "tuv", hash['9'] = "wxyz";
        int n = digits.size();
        auto dfs = [&](auto&& self, int sta, vector<string>& res, string& pack) -> void
        {
            if (sta == n)
            {
                if (pack.size())
                    res.emplace_back(pack);
                return;
            }
            for (int i = 0; i < hash[digits[sta]].size(); i ++ )
            {
                pack += hash[digits[sta]][i];
                sta += 1;
                self(self, sta, res, pack);
                sta -= 1;
                pack.pop_back();
            }
        };
        vector<string> res;
        string pack = "";
        dfs(dfs, 0, res, pack);
        return res;
    }
};
// @lc code=end

