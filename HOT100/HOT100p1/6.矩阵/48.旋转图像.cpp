/*
 * @lc app=leetcode.cn id=48 lang=cpp
 *
 * [48] 旋转图像
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; i ++ )
        {
            for (int j = 0; j < i; j ++ )
            {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (auto& row : matrix)
        {
            ranges::reverse(row);
        }
    }
};
// @lc code=end

class Solution {
    public:
        void rotate(vector<vector<int>>& matrix) {
            int m = matrix.size() - 1, n = matrix[0].size() - 1;
            int l = 0, r = n, t = 0, b = m;
            int left = 0, right = n;
            while (left <= right && l <= r && t <= b)
            {
                for (int i = left; i < right; i ++ )
                {
                    int tmp = matrix[t][l + i];
                    matrix[t][l + i] = matrix[b - i][l];
                    matrix[b - i][l] = matrix[b][r - i];
                    matrix[b][r - i] = matrix[t + i][r];
                    matrix[t + i][r] = tmp;
                }
                l ++, r --, t ++, b --;
                right -= 2;
            }
        }
    };