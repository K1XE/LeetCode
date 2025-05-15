/*
 * @lc app=leetcode.cn id=2900 lang=cpp
 *
 * [2900] 最长相邻不相等子序列 I
 */
#include "tools.h"

// @lc code=start
class Solution
{
public:
    vector<string> getLongestSubsequence(vector<string> &words, vector<int> &groups)
    {
        vector<string> res;
        res.emplace_back(words[0]);
        int lastvis = 0;
        for (int i = 1; i < groups.size(); i ++ )
        {
            if (groups[i] != groups[lastvis])
            {
                res.emplace_back(words[i]);
                lastvis = i;
            }
        }
        return res;
    }
};
// @lc code=end

class Solution
{
public:
    vector<string> getLongestSubsequence(vector<string> &words, vector<int> &groups)
    {
        vector<pair<string, int>> res;
        res.emplace_back(words[0], groups[0]);
        for (int i = 1; i < groups.size(); i ++ )
        {
            if (groups[i] != res.back().second)
            {
                res.emplace_back(words[i], groups[i]);
            }
        }
        vector<string> ans;
        for (auto psi : res)
        {
            ans.push_back(psi.first);
        }
        return ans;
    }
};

class Solution
{
public:
    vector<string> getLongestSubsequence(vector<string> &words, vector<int> &groups)
    {
        int n = groups.size();
        vector<pair<int, int>> pack;
        vector<pair<int, int>> res;
        auto dfs = [&](auto &&self, int sta) -> void
        {
            if (sta == n)
            {
                if (pack.size() > res.size())
                {
                    res = pack;
                }
                return;
            }
            for (int i = sta; i < n; i++)
            {
                if (pack.size() && groups[i] == pack.back().first)
                    continue;
                if (!pack.size() || groups[i] != pack.back().first)
                {
                    pack.emplace_back(groups[i], i);
                    self(self, i + 1);
                    pack.pop_back();
                }
            }
        };
        dfs(dfs, 0);
        vector<string> ans;
        for (auto &pii : res)
        {
            ans.push_back(words[pii.second]);
        }
        return ans;
    }
};