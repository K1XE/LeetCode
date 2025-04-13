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
        get_next(needle, next);
        int i = 0, j = 0;
        while (i < haystack.size())
        {
            if (haystack[i] == needle[j])
            {
                i ++, j ++;
                if (j == needle.size()) return i - j;
            }
            else
            {
                if (j > 0)  j = next[j - 1];
                else i ++;
            }
        }
        return -1;
    }
private:
    void get_next(string& s, vector<int>& next)
    {
        int j = 0;
        next[0] = 0;
        for (int i = 1; i < s.size();  i++ )
        {
            while (j > 0 && s[j] != s[i])
            {
                j = next[j - 1];
            }
            if (s[j] == s[i]) j ++;
            next[i] = j;
        }
        return;
    }
};

// @lc code=end
class Solution {
    public:
        int strStr(string haystack, string needle) {
            int i = 0;
            int loop = haystack.size() - needle.size();
            while (i <= loop)
            {
                bool flag = 0;
                for (int cnt1 = i, cnt2 = 0;  cnt2 < needle.size(); cnt1 ++, cnt2 ++)
                {
                    if (haystack[cnt1] != needle[cnt2])
                    {
                        flag = 1;
                        break;
                    }
                }
                if (!flag) return i;
                i ++;
            }
            return -1;
        }
    };
