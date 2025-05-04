/*
 * @lc app=leetcode.cn id=1128 lang=cpp
 *
 * [1128] 等价多米诺骨牌对的数量
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        int cnt[10][10] = {};
        int res = 0;
        for (auto& d : dominoes)
        {
            auto [a, b] = minmax(d[0], d[1]);
            res += cnt[a][b];
            cnt[a][b] ++;
        }
        return res;
    }
};
// @lc code=end

