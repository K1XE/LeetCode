/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 找出字符串中第一个匹配项的下标
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int strStr(string haystack, string needle) {
        vector<int> next(needle.size());
        getNext(needle, next);
        int i = 0, j = 0;
        while (i < haystack.size())
        {
            if (haystack[i] != needle[j])
            {
                if (j > 0) j = next[j - 1];
                else j = 0, i ++;
            }
            else
            {
                while (haystack[i] == needle[j])
                {
                    i ++, j ++;
                    if (j == needle.size()) return i - j;
                }
            }
        }
        return -1;
    }
private:
    void getNext(string s, vector<int>& next)
    {
        int j = 0;
        next[0] = 0;
        for (int i = 1; i < s.size(); i ++ )
        {
            while (j > 0 && s[j] != s[i]) j = next[j - 1];
            if (s[j] == s[i]) j ++;
            next[i] = j;
        }
    }
};
// @lc code=end

