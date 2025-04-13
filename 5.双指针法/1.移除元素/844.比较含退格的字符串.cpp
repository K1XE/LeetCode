/*
 * @lc app=leetcode.cn id=844 lang=cpp
 *
 * [844] 比较含退格的字符串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        short hps = 0, hpt = 0, ps = s.size() - 1, pt = t.size() - 1;
        while (pt >= 0 || ps >= 0)
        {
            while (ps >= 0)
            {
                if (s[ps] == '#')
                {
                    ps --, hps ++;
                }
                else
                {
                    if (hps) ps --, hps --;
                    else break;
                }
            }
            while (pt >= 0)
            {
                if (t[pt] == '#')
                {
                    pt --, hpt ++;
                }
                else
                {
                    if (hpt) pt --, hpt --;
                    else break;
                }
            }
            if (ps >= 0 && pt >= 0)
            {
                if (s[ps] != t[pt]) return 0;
                else ps --, pt --;
            }
            else
            {
                if (ps >= 0 || pt >= 0) return 0;
            }
        }
        return 1;
    }
};
// @lc code=end

