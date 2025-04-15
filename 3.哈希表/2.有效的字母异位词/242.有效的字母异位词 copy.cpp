/*
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
    public:
        bool isAnagram(string s, string t) {
            array<int, 26> hash{};
            for (auto c : s)
            {
                hash[c - 'a'] ++; 
            }
            for (auto c : t)
            {
                hash[c - 'a'] --;
            }
            for (int i = 0; i < hash.size(); i ++ )
            {
                if (hash[i] != 0) return 0;
            }
            return 1;
        }
    };
// @lc code=end
