/*
 * @lc app=leetcode.cn id=240 lang=cpp
 *
 * [240] 搜索二维矩阵 II
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int i = 0, j = n - 1;
        if (! m || ! n) return 0;
        while (i < m && j >= 0)
        {
            if (matrix[i][j] == target) return 1;
            else if (matrix[i][j] > target) j --;
            else i ++;
        }
        return 0;
    }
};
// @lc code=end

