/*
 * @lc app=leetcode.cn id=541 lang=cpp
 *
 * [541] 反转字符串 II
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string reverseStr(string s, int k) {
        int step = 0;
        while (step < s.size())
        {
            int l = step, r = step + k - 1;
            if (r >= s.size()) r = s.size() - 1;
            while (l < r)
            {
                swap(s[l ++], s[r --]);
            }
            step += 2*k;
        }
        return s;
    }
};
// @lc code=end

