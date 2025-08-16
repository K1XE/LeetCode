/*
 * @lc app=leetcode.cn id=73 lang=cpp
 *
 * [73] 矩阵置零
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool _m0flag = 0, _n0flag = 0;
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < m; i ++ )
        {
            if (matrix[i][0] == 0) 
            {
                _m0flag = 1;
                break;
            }
        }
        for (int j = 0; j < n; j ++ )
        {
            if (matrix[0][j] == 0)
            {
                _n0flag = 1;
                break;
            }
        }
        for (int i = 1; i < m; i ++ )
        {
            for (int j = 1; j < n; j ++ )
            {
                if (matrix[i][j] == 0)
                {
                    matrix[0][j] = matrix[i][0] = 0;
                }
            }
        }
        for (int i = 1; i < m; i ++ )
        {
            for (int j = 1; j < n; j ++ )
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        if (_m0flag)
        {
            for (int i = 0; i < m; i ++ )
            {
                matrix[i][0] = 0;
            }
        }
        if (_n0flag)
        {
            for (int j = 0; j < n; j ++ )
            {
                matrix[0][j] = 0;
            }
        }
    }
};
// @lc code=end

