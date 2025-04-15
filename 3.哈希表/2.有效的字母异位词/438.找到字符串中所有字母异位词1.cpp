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
        array<int, 26> hash{};
        array<int, 26> hash_s{};
        vector<int> res;
        int i = 0;
        for (auto c : p) hash[c - 'a'] ++;
        for (int j = 0; j < s.size(); j ++ )
        {
            if (hash[s[j] - 'a'] != 0) hash_s[s[j] - 'a'] ++;
            if (j - i + 1 == p.size())
            {
                if (hash_s == hash) res.push_back(i);
                if (hash[s[i] - 'a'] != 0) hash_s[s[i] - 'a'] --;
                i ++;
            }
        }
        return res;
    }
};
// @lc code=end

// WHY
class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            unordered_map<char, int> hash;
            vector<int> res;
            for (auto c : p) hash[c] ++;
            int valid = 0;
            int i = 0;
            for (int j = 0; j < s.size(); j ++ )
            {
                if (hash.find(s[j]) != hash.end())
                {
                    if (-- hash[s[j]] == 0) valid ++;
                }
                if (j - i + 1 == p.size())
                {
                    if (valid == hash.size())
                    {
                        res.push_back(i);
                    }
                    if (hash.find(s[i]) != hash.end())
                    {
                        if (++ hash[s[i]] > 0) valid --;
                    }
                    i ++;
                }
            }
            return res;
        }
    };