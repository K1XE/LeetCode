/*
 * @lc app=leetcode.cn id=79 lang=cpp
 *
 * [79] 单词搜索
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> vis(m, vector<bool>(n, 0));
        vector<pair<int, int>> dis = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        auto dfs = [&](auto&& self, int x, int y, int cur) -> bool
        {
            if (board[x][y] != word[cur]) return 0;
            if (cur == word.size() - 1)
            {
                return board[x][y] == word.back();
            }
            vis[x][y] = 1;
            for (auto d : dis)
            {
                
                int nx = x + d.first, ny = y + d.second;
                if (0 <= nx && nx < m && 0 <= ny && ny < n && !vis[nx][ny])
                {
                    cur += 1;
                    bool res = self(self, nx, ny, cur);
                    if (res) return 1;
                    cur -= 1;
                }
            }
            vis[x][y] = 0;
            return 0;
        };
        
        for (int i = 0; i < m; i ++ )
            for (int j = 0; j < n; j ++ )
                if (dfs(dfs, i, j, 0)) return 1;
        return 0;
    }
};
// @lc code=end

