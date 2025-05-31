/*
 * @lc app=leetcode.cn id=1931 lang=cpp
 *
 * [1931] 用三种不同颜色为网格涂色
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int MOD = 1'000'000'007;
    int colorTheGrid(int m, int n) {
        auto check_col = [&](vector<int>& vec) -> bool
        {
            for (int i = 1; i < m; i ++ )
            {
                if (vec[i] == vec[i - 1]) return 0;
            }
            return 1;
        };

        auto check_row = [&](vector<int>& a, vector<int>& b) -> bool
        {
            for (int i = 0; i < m; i ++ )
            {
                if (a[i] == b[i]) return 0;
            }
            return 1;
        };

        auto encode = [&](vector<int>& vec) -> int
        {
            int res = 0;
            for (int i = 0; i < m; i ++ )
            {
                res = res * 3 + vec[i];
            }
            return res;
        };

        vector<vector<int>> valid;
        auto dfs = [&](auto&& self, vector<int>& vec, int depth) -> void
        {
            if (depth == m)
            {
                if (check_col(vec)) valid.emplace_back(vec);
                return; 
            }
            
            for (int i = 0; i < 3; i ++ )
            {
                if (depth > 0 && vec[depth - 1] == i) continue;
                vec[depth] = i;
                self(self, vec, depth + 1);
            }
        };

        vector<int> vec(m);
        dfs(dfs, vec, 0);

        unordered_map<int, vector<int>> nxt_valid;
        int vn = valid.size();
        for (int i = 0; i < vn; i ++ )
        {
            for (int j = 0; j < vn; j ++ )
            {
                if (check_row(valid[i], valid[j]))
                {
                    nxt_valid[encode(valid[i])].push_back(encode(valid[j]));
                }
            }
        }

        unordered_map<int, int>dp;
        for (auto& s : valid)
        {
            dp[encode(s)] = 1;
        }

        for (int cols = 1; cols < n; cols ++ )
        {
            unordered_map<int, int> nxt_dp;
            for (auto& [pre_code, cnt] : dp)
            {
                for (auto& nxt_code : nxt_valid[pre_code])
                {
                    nxt_dp[nxt_code] = (nxt_dp[nxt_code] + cnt) % MOD;
                }
            }
            dp = nxt_dp;
        }
        int res = 0;
        for (auto& [_, cnt] : dp) res = (res + cnt) % MOD;
        return res;
    }
};
// @lc code=end

