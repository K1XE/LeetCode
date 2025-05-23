/*
 * @lc app=leetcode.cn id=37 lang=cpp
 *
 * [37] 解数独
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<int>> row_vis(9, vector<int>(10, 0));
        vector<vector<int>> col_vis(9, vector<int>(10, 0));
        vector<vector<int>> box_vis(9, vector<int>(10, 0));
        vector<pair<int, int>> _e;
        for (int i = 0; i < 9; i ++ )
        {
            for (int j = 0; j < 9; j ++ )
            {
                int box_idx = i / 3 * 3 + j / 3;
                if (board[i][j] != '.')
                {
                    int _x = board[i][j] - '0';
                    row_vis[i][_x] = 1;
                    col_vis[j][_x] = 1;
                    box_vis[box_idx][_x] = 1;
                }
                else
                {
                    _e.emplace_back(i, j);
                }
            }
        }
        auto dfs = [&](auto&& self, int pos) -> bool
        {
            if (pos == _e.size()) return 1;
            auto d = _e[pos];
            int x = d.first, y = d.second;
            int bi = x / 3 * 3 + y / 3;
            for (int i = 1; i < 10; i ++ )
            {
                if (!row_vis[x][i] && !col_vis[y][i] && !box_vis[bi][i])
                {
                    row_vis[x][i] = 1, col_vis[y][i] = 1, box_vis[bi][i] = 1;
                    board[x][y] = i + '0';
                    if (self(self, pos + 1)) return 1;
                    board[x][y] = '.';
                    row_vis[x][i] = 0, col_vis[y][i] = 0, box_vis[bi][i] = 0;
                }
            }
            return 0;
        };
        bool tmp = dfs(dfs, 0);
    }
};
// @lc code=end

