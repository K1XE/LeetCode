/*
 * @lc app=leetcode.cn id=383 lang=cpp
 *
 * [383] 赎金信
 */

// @lc code=start
class Solution {
    public:
        bool canConstruct(string ransomNote, string magazine) {
            array<int, 26> hash{};
            for (auto c : magazine)
            {
                hash[c - 'a'] ++;
            }
            for (auto c : ransomNote)
            {
                if (hash[c - 'a'] <= 0) return 0;
                else hash[c - 'a'] --;
            }
            return 1;
        }
    };
// @lc code=end
class Solution {
    public:
        bool canConstruct(string ransomNote, string magazine) {
            unordered_map<char, int> hash;
            for (auto c : magazine)
            {
                hash[c] ++;
            }
            for (auto c : ransomNote)
            {
                if (hash.find(c) == hash.end()) return 0;
                if (hash[c] > 0) hash[c] --;
                else return 0;
            }
            return 1;
        }
    };
