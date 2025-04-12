/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */

// @lc code=start
class Solution {
    public:
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
            int l = 0, r = matrix[0].size() - 1, t = 0, b = matrix.size() - 1;
            vector<int> res;
            while (1)
            {
                for (int i = l; i <= r; i ++ )
                {
                    res.push_back(matrix[t][i]);
                }
                if (++ t > b) break;
                for (int i = t; i <= b; i ++ )
                {
                    res.push_back(matrix[i][r]);
                }
                if (-- r < l) break;
                for (int i = r; i >= l; i -- )
                {
                    res.push_back(matrix[b][i]);
                }
                if (-- b < t) break;
                for (int i = b; i >= t; i -- )
                {
                    res.push_back(matrix[i][l]);
                }
                if (++ l > r) break;
    
            }
            return res;
    
        }
    };
// @lc code=end

class Solution {
    public:
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
            vector<int> res;
            int m = matrix.size();
            int n = matrix[0].size();
            int vcnt = m * n;
            int sx = 0, sy = 0, offset = 1;
            while (vcnt - 1 > 0)
            {
                int i = sx, j = sy;
                for (; j < n - offset; j ++ )
                {
                    res.push_back(matrix[i][j]);
                    vcnt --;
                    if (vcnt - 1 < 0) return res;
                }
                for (; i < m - offset; i ++ )
                {
                    res.push_back(matrix[i][j]);
                    vcnt --;
                    if (vcnt - 1 < 0) return res;
                }
                for (; j > sy; j -- )
                {
                    res.push_back(matrix[i][j]);
                    vcnt --;
                    if (vcnt - 1 < 0) return res;
                }
                for (; i > sx; i -- )
                {
                    res.push_back(matrix[i][j]);
                    vcnt --;
                    if (vcnt - 1 < 0) return res;
                }
                sx ++, sy ++, offset ++;
            }
            if (vcnt == 1)
            {
                int midm = m / 2, midn = n / 2;
                res.push_back(matrix[midm][midn]);
            }
    
            return res;
        }
    };