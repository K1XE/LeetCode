/*
 * @lc app=leetcode.cn id=459 lang=cpp
 *
 * [459] 重复的子字符串
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        vector<int> next(s.size());
        getNext(s, next);
        int len = s.size();
        if (next[len - 1] > 0 && len % (len - next[len - 1]) == 0) return 1;
        return 0;
    }
private:
    void getNext(string s, vector<int>& next)
    {
        int j = 0;
        next[0] = 0;
        for (int i = 1; i < s.size(); i ++ )
        {
            while (j > 0 && s[j] != s[i]) j = next[j - 1];
            if (s[i] == s[j]) j ++;
            next[i] = j;
        }
    }
};
// @lc code=end

