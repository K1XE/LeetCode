/*
 * @lc app=leetcode.cn id=151 lang=cpp
 *
 * [151] 反转字符串中的单词
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string reverseWords(string s) {
        int l = 0, r = s.size() - 1;
        string res;
        while (l <= r && s[l] == ' ') l ++;
        while (l <= r)
        {
            while (l <= r && s[r] == ' ')
            {
                r --;
            }
            string strr;
            while (l <= r && s[r] != ' ')
            {
                strr += s[r --];
            }
            reverse(strr.begin(), strr.end());
            res += strr.append(" ");
        }
        res.pop_back();
        return res;
    }
};
// @lc code=end

