/*
 * @lc app=leetcode.cn id=77 lang=cpp
 *
 * [77] 组合
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> pack;
        dfs(1, n, k, res, pack);
        return res;
    }
    void dfs(int sta, int n, int k, vector<vector<int>>& res, vector<int>& pack)
    {
        if (pack.size() == k)
        {
            res.emplace_back(pack);
            return;
        }
        for (int i = sta; i <= n - (k - pack.size()) + 1; i ++ )
        {
            pack.push_back(i);
            dfs(i + 1, n, k, res, pack);
            pack.pop_back();
        }
    }
};
// @lc code=end

