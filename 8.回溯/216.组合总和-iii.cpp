/*
 * @lc app=leetcode.cn id=216 lang=cpp
 *
 * [216] 组合总和 III
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> pack;
        dfs(res, pack, 1, k, 0, n);
        return res;
    }
    void dfs(vector<vector<int>>& res, vector<int>& pack, int sta, int k, int sums, int n)
    {
        if (pack.size() == k)
        {
            if (sums == n)
            {
                res.emplace_back(pack);
            }
            return;
        }
        for (int i = sta; i <= 9; i ++ )
        {
            sums += i;
            if (sums > n)
            {
                sums -= i;
                break;
            }
            pack.push_back(i);
            dfs(res, pack, i + 1, k, sums, n);
            pack.pop_back();
            sums -= i;
        }
    }
};
// @lc code=end

