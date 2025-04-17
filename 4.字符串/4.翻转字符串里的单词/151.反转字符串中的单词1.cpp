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
        delSpace(s);
        reverseString(s, 0, s.size() - 1);
        int sta = 0;
        for (int j = 0; j <= s.size(); j ++ )
        {
            if (j == s.size() || s[j] == ' ')
            {
                reverseString(s, sta, j - 1);
                sta = j + 1;
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
    void delSpace(string& s)
    {
        int slow = 0;
        for (int i = 0; i < s.size(); i ++ )
        {
            if (s[i] != ' ')
            {
                if (slow > 0) s[slow ++] = ' ';
                while (i < s.size() && s[i] != ' ') s[slow ++] = s[i ++];
            }
        }
        s.resize(slow);
    }
};
// @lc code=end

