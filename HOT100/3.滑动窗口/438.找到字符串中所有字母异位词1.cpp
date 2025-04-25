/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start

class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            unordered_map<char, int> hash;
            vector<int> res;
            for (auto c : p)
            {
                hash[c] ++;
            }
            int i = 0;
            int valid = 0, need = hash.size();
            for (int j = 0; j < s.size(); j ++ )
            {
                if (hash.count(s[j]))
                {
                    if (-- hash[s[j]] == 0) valid ++;
                }
                if (j - i + 1 == p.size())
                {
                    if (valid == need)
                    {
                        res.push_back(i);
                    }
                    if (hash.count(s[i]))
                    {
                        if (hash[s[i]] ++ == 0) valid --;
                    }
                    i ++;
                }
            }
            return res;
        }
    };
// @lc code=end


class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            unordered_map<char, int> hash, hash_s;
            vector<int> res;
            for (auto c : p)
            {
                hash[c] ++;
            }
            int i = 0;
            for (int j = 0; j < s.size(); j ++ )
            {
                hash[s[j]] --;
                while (hash[s[j]] < 0)
                {
                    hash[s[i ++]] ++;
                }
                if (j - i + 1 == p.size())
                {
                    res.push_back(i);
                }
            }
            return res;
        }
    };

class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            unordered_map<char, int> hash, hash_s;
            vector<int> res;
            for (auto c : p)
            {
                hash[c] ++;
            }
            int i = 0;
            for (int j = 0; j < s.size(); j ++ )
            {
                if (hash.find(s[j]) != hash.end()) hash_s[s[j]] ++;
                if (j - i + 1 == p.size())
                {
                    if (hash_s == hash) res.push_back(i);
                    if (hash.find(s[i]) != hash.end()) hash_s[s[i]] --;
                    i ++;
                }
            }
            return res;
        }
    };

class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            unordered_map<char, int> hash;
            vector<int> res;
            for (auto c : p)
            {
                hash[c] ++;
            }
            int i = 0;
            int valid = 0, need = hash.size();
            for (int j = 0; j < s.size(); j ++ )
            {
                if (hash.find(s[j]) != hash.end())
                {
                    hash[s[j]] --;
                    if (hash[s[j]] == 0) valid ++;
                }
                if (j - i + 1 == p.size())
                {
                    if (valid == need)
                    {
                        res.push_back(i);
                    }
                    if (hash.find(s[i]) != hash.end())
                    {
                        hash[s[i]] ++;
                        if (hash[s[i]] >= 0) valid --;
                    }
                    i ++;
                }
            }
            return res;
        }
    };