/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
class Solution {
    public:
        vector<vector<int>> generateMatrix(int n) {
            vector<vector<int>> res(n, vector<int>(n, 0));
            int sx = 0, sy = 0, offset = 1, cnt = 1, times = n / 2;
            while ( times -- )
            {
                int j = sy, i = sx;
                for (; j < n - offset; j ++ )
                {
                    res[i][j] = cnt ++;
                }
                for (; i < n - offset; i ++ )
                {
                    res[i][j] = cnt ++;
                }
                for (; j > sy; j -- )
                {
                    res[i][j] = cnt ++;
                }
                for (; i > sx; i -- )
                {
                    res[i][j] = cnt ++;
                }
                sy ++, sx ++, offset ++;
            }
            int mid = n / 2;
            if (n % 2) res[mid][mid] = cnt;
            return res;
        }
    
    };
// @lc code=end

