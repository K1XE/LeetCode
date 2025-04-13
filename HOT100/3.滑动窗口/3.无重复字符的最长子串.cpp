/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0, j = 0;
        int maxLen = 0;
        unordered_map<char, int> hash;
        for (; j < s.size(); j ++ )
        {
            hash[s[j]] ++;
            while (hash[s[j]] > 1)
            {
                hash[s[i ++]] --;
            }
            maxLen = max(maxLen, j - i + 1);
        }
        return maxLen;
    }
};
// @lc code=end

