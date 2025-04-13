/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 */

// @lc code=start
class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            array<int, 26> hash{};
            vector<int> res;
            for (auto c : p)
            {
                hash[c - 'a'] ++;
            }
            int i = 0, j = 0;
            for (; j < s.size(); j ++ )
            {
                hash[s[j] - 'a'] --;
                while (hash[s[j] - 'a'] < 0)
                {
                    hash[s[i] - 'a'] ++;
                    i ++;
                }
                if (j - i + 1 == p.size()) res.push_back(i);
            }
            return res;
        };
};
// @lc code=end
class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            array<int, 26> hash_s{}, hash_p{};
            vector<int> res;
            for (auto c : p)
            {
                hash_p[c - 'a'] ++;
            }
            int j = 0;
            for (; j < s.size(); j ++ )
            {
                hash_s[s[j] - 'a'] ++;
                int i = j - p.size() + 1;
                if (i < 0) continue;
                if (hash_s == hash_p) res.push_back(i);
                hash_s[s[i] - 'a'] --;
            }
            return res;
        }
    };
class Solution {
    public:
        vector<int> findAnagrams(string s, string p) {
            unordered_map<char, int> hash_p, hash_s;
            vector<int> res;
            for (auto c : p)
            {
                hash_p[c] ++;
            }
            int i = 0, j = 0;
            for (; j < s.size(); j ++)
            {
                hash_s[s[j]] ++;
                if (j - i + 1 == p.size())
                {
                    if (hash_s == hash_p)
                    {
                        res.push_back(i);
                    }
                    hash_s[s[i]] --;
                    if (hash_s[s[i]] == 0) hash_s.erase(s[i]);
                    i ++;
                }
            }
            return res;
        }
    };