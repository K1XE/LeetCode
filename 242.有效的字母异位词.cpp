/*
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
class Solution {
    public:
        bool isAnagram(string s, string t) {
            unordered_map<char, int> hash;
            for (auto c : s)
            {
                hash[c] ++;
            }
            for (auto c : t)
            {
                hash[c] --;
                if (hash[c] == 0) hash.erase(c);
            }
            return hash.size() == 0 ? 1 : 0;
        }
    };
// @lc code=end
class Solution {
    public:
        bool isAnagram(string s, string t) {
            unordered_map<char, int> hash_s, hash_t;
            for (auto c : s)
            {
                hash_s[c] ++;
            }
            for (auto c : t)
            {
                hash_t[c] ++;
            }
            return hash_s == hash_t;
        }
    };
