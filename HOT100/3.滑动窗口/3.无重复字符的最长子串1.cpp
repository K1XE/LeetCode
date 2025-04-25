/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hash;
        int i = 0, maxLen = 0;
        for (int j = 0; j < s.size(); j ++ )
        {
            hash[s[j]] ++;
            if (hash[s[j]] == 1) maxLen = max(maxLen, j - i + 1);
            while (hash[s[j]] > 1)
            {
                hash[s[i]] --;
                if (hash[s[i]] == 0) hash.erase(s[i]);
                i ++;
            }
            maxLen = max(maxLen, j - i + 1);
        }
        return maxLen;
    }
};
// @lc code=end

