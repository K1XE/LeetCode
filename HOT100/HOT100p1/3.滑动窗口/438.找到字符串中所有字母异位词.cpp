/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int i = 0, j = 0;
        array<int, 26> hash_p{};
        vector<int> res;
        for (auto c : p)
        {
            hash_p[c - 'a'] ++;
        }
        for (; j < s.size(); j ++ )
        {
            hash_p[s[j] - 'a'] --;
            while (hash_p[s[j] - 'a'] < 0)
            {
                hash_p[s[i ++] - 'a'] ++;
            }
            if (j - i + 1 == p.size()) res.push_back(i);
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            int i = 0, j = 0;
            array<int, 26> hash_p{}, hash_s{};
            vector<int> res;
            for (auto c : p)
            {
                hash_p[c - 'a'] ++;
            }
            while (j < s.size())
            {
                hash_s[s[j] - 'a'] ++;
                if (j - i + 1 == p.size())
                {
                    if (hash_p == hash_s) res.push_back(i);
                    hash_s[s[i ++] - 'a'] --;
                }
                j ++;
            }
            return res;
        }
    };
