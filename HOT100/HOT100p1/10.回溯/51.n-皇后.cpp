/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N 皇后
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {

        vector<vector<string>> res;
        vector<string> pack(n);
        string s = "";
        for (int i = 0; i < n; i ++ )
        {
            s += '.';
        }
        for (int i = 0; i < n; i ++ )
        {
            pack[i] = s;
        }
        auto check = [&](int row, int col) -> bool
        {
            for (int i = 0; i < row; i ++ )
            {
                if (pack[i][col] == 'Q') return 0;
            }

            for (int j = 0; j < col; j ++ )
            {
                if (pack[row][j] == 'Q') return 0;
            }
            for (int i = row, j = col; i >= 0 && j >= 0; i --, j -- )
            {
                if (pack[i][j] == 'Q') return 0;
            }
            for (int i = row, j = col; i >= 0 && j < n; i --, j ++ )
            {
                if (pack[i][j] == 'Q') return 0;
            }
            return 1;
        };

        auto dfs = [&](auto&& self, int row) -> void
        {
            if (row == n)
            {
                res.emplace_back(pack);
                return;
            }
            for (int col = 0; col < n; col ++ )
            {
                if (!check(row, col)) continue;
                pack[row][col] = 'Q';
                self(self, row + 1);
                pack[row][col] = '.';
            }
        };
        dfs(dfs, 0);
        return res;
    }
};
// @lc code=end

