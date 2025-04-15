/*
 * @lc app=leetcode.cn id=383 lang=cpp
 *
 * [383] 赎金信
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        array<int, 26> hash;
        for (auto c : magazine) hash[c - 'a'] ++;
        for (auto c : ransomNote)
        {
            if (-- hash[c - 'a'] < 0) return 0;
        }
        return 1;
    }
};
// @lc code=end

