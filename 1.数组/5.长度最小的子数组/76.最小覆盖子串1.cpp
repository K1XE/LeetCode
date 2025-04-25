/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> hash;
        for (auto c : t)
        {
            hash[c] ++;
        }
        int i = 0;
        int valid = 0, need = hash.size();
        int minLen = INT_MAX, sta = -1;
        for (int j = 0; j < s.size(); j ++ )
        {
            if (hash.find(s[j]) != hash.end())
            {
                if (-- hash[s[j]] == 0) valid ++;
            }
            while (valid == need)
            {
                int len = j - i + 1;
                
                if (minLen > len)
                {
                    minLen = len, sta = i;
                }
                if (hash.find(s[i]) != hash.end())
                {
                    if (++ hash[s[i]] > 0) valid --;
                }
                i ++;
            }
        }
        return sta == -1 ? "" : s.substr(sta, minLen);
    }
};
// @lc code=end

