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
        for (int i = 0; i < s.size(); i += 2 * k )
        {
            if (i + k - 1 >= s.size())
            {
                reverseString(s, i, s.size() - 1);
            }
            else
            {
                reverseString(s, i, i + k - 1);
            }
        }
        return s;
    }
private:
    void reverseString(string& s, int l, int r)
    {
        while (l <= r)
        {
            swap(s[l ++], s[r --]);
        }
    }
};
// @lc code=end

