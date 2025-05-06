/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        ranges::sort(candidates);
        vector<vector<int>> res;
        vector<int> pack;
        dfs(0, res, pack, 0, target, candidates);
        return res;
    }
    void dfs(int sta, vector<vector<int>>& res, vector<int>& pack, int sums, int t, vector<int>& c)
    {
        if (sums == t)
        {
            res.emplace_back(pack);
            return;
        }
        for (int i = sta; i < c.size(); i ++ )
        {
            sums += c[i];
            if (sums > t) break;
            pack.push_back(c[i]);
            dfs(i, res, pack, sums, t, c);
            pack.pop_back();
            sums -= c[i];
        }
    }
};
// @lc code=end

