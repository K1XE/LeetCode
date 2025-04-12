/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class Solution {
    public:
        string minWindow(string s, string t) {
            unordered_map<char, int> hash_t;
            unordered_map<char, int> hash_s;
            for (char ch : t) {
                hash_t[ch]++;
            }
            int i = 0, len = INT_MAX, minLen = INT_MAX, start = -1, end = -1;
            int valid = 0;
            for (int j = 0; j < s.size(); j++) {
                char c = s[j];
                if (hash_t.count(c))
                {
                    hash_s[c] ++;
                    if (hash_s[c] == hash_t[c]) valid ++;
                }
    
                while (valid == hash_t.size())
                {
                    len = j - i + 1;
                    if (len < minLen)
                    {
                        start = i;
                        end = j;
                        minLen = len;
                    }
                    char d = s[i ++ ];
                    if (hash_t.count(d))
                    {
                        hash_s[d] --;
                        if (hash_s[d] < hash_t[d]) valid --;
                    }
                }
    
            }
            return minLen == INT32_MAX ? "" : s.substr(start, minLen);
        }
    
    };
// @lc code=end

class Solution {
    public:
        string minWindow(string s, string t) {
            unordered_map<char, int> hash_t;
            unordered_map<char, int> hash_s;
            for (char ch : t) {
                hash_t[ch]++;
            }
            int i = 0, len = INT_MAX, minLen = INT_MAX, start = -1, end = -1;
            for (int j = 0; j < s.size(); j++) {
                hash_s[s[j]]++;
                while (isSubHash(hash_t, hash_s)) {
                    len = j - i + 1;
                    if (len < minLen) {
                        start = i;
                        end = j;
                        minLen = len;
                    }
                    hash_s[s[i]]--;
                    i++;
                }
            }
            if (start == -1 && end == -1) return "";
            return s.substr(start, minLen);
        }
    
    private:
        bool isSubHash(const unordered_map<char, int>& small, const unordered_map<char, int>& big) {
            for (const auto& [key, val] : small) {
                if (big.find(key) == big.end() || big.at(key) < val) {
                    return false;
                }
            }
            return true;
        }
    };