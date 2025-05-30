/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int l = 0, r = n - 1, t = 0, b = m - 1;
        vector<int> res;
        while (1)
        {
            for (int i = l; i <= r; i ++ ) res.push_back(matrix[t][i]);
            if (++ t > b) break;
            for (int i = t; i <= b; i ++ ) res.push_back(matrix[i][r]);
            if (-- r < l) break;
            for (int i = r; i >= l; i -- ) res.push_back(matrix[b][i]);
            if (-- b < t) break;
            for (int i = b; i >= t; i -- ) res.push_back(matrix[i][l]);
            if (++ l > r) break;
        }
        return res;
    }
};
// @lc code=end

