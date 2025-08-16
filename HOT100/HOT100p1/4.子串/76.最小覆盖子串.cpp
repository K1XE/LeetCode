/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string minWindow(string s, string t) {
        int i = 0;
        unordered_map<char, int> hash;
        for (auto c : t)
        {
            ++ hash[c];
        }
        int valid = 0, minLen = INT32_MAX, start = -1;
        for (int j = 0; j < s.size(); j ++ )
        {
            if (hash.find(s[j]) != hash.end())
            {
                if(-- hash[s[j]] == 0) valid ++;
            }
            while (valid == hash.size())
            {
                if (j - i + 1 < minLen)
                {
                    start = i;
                    minLen = j - i + 1;
                }
                if (hash.find(s[i]) != hash.end())
                {
                    if (++ hash[s[i]] > 0) valid --;
                }
                i ++;
            }
        }
        return start == -1 ? "" : s.substr(start, minLen);
    }
};
// @lc code=end

