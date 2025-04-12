/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
class Solution {
    public:
        vector<vector<int>> generateMatrix(int n) {
            int l = 0, r = n - 1, t = 0, b = n - 1;
            int cnt = 1;
            vector<vector<int>> res(n, vector<int> (n, 0));
            while (1)
            {
                for (int i = l; i <= r; i ++ )
                {
                    res[t][i] = cnt ++;
                }
                if (++ t > b) break;
                for (int i = t; i <= b; i ++ )
                {
                    res[i][r] = cnt ++;
                }
                if (-- r < l) break;
                for (int i = r; i >= l; i -- )
                {
                    res[b][i] = cnt ++;
                }
                if (-- b < t) break;
                for (int i = b; i >= t; i -- )
                {
                    res[i][l] = cnt ++;
                }
                if (++ l > r) break;
            }
            return res;
        }
    
    };
// @lc code=end

