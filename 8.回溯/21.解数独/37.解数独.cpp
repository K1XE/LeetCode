/*
 * @lc app=leetcode.cn id=37 lang=cpp
 *
 * [37] 解数独
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<int>> row_used(9, vector<int>(9, 0)), 
                            col_used(9, vector<int>(9, 0)),
                            box_used(9, vector<int>(9, 0));
        vector<pair<int, int>> _empty;
        for (int row = 0; row < 9; row ++ )
        {
            for (int col = 0; col < 9; col ++ )
            {
                if (board[row][col] == '.') _empty.emplace_back(row, col);
                else
                {
                    int x = board[row][col] - '1';
                    row_used[row][x] = 1;
                    col_used[col][x] = 1;
                    box_used[row / 3 * 3 + col / 3][x] = 1;
                }
            }
        }
        auto check = [&](int row, int col, int x) -> bool
        {
            return !row_used[row][x] && !col_used[col][x] && !box_used[row / 3 * 3 + col / 3][x];
        };

        auto dfs = [&](auto&& self, int pos) -> bool
        {
            if (pos == _empty.size()) return 1;
            auto [row, col] = _empty[pos];
            for (int x = 0; x < 9; x ++ )
            {
                int box_idx = row / 3 * 3 + col / 3;
                if (check(row, col, x))
                {
                    row_used[row][x] = 1;
                    col_used[col][x] = 1;
                    box_used[box_idx][x] = 1;
                    board[row][col] = x + '1';
                    if (self(self, pos + 1)) return 1;
                    board[row][col] = '.';
                    row_used[row][x] = 0;
                    col_used[col][x] = 0;
                    box_used[box_idx][x] = 0;
                }
            }
            return 0;
        };
        dfs(dfs, 0);
    }
};
// @lc code=end

