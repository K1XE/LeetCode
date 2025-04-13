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
            for (auto c : t)
            {
                hash_t[c] ++;
            }
            int valid = 0;
            int need = hash_t.size();
            int i = 0, j = 0, start = -1, end = -1;
            int len = INT32_MAX, minLen = INT32_MAX;
            for (; j < s.size(); j ++ )
            {
                if (hash_t.find(s[j]) != hash_t.end())
                {
                    hash_t[s[j]] --;
                    if (hash_t[s[j]] == 0)
                    {
                        valid ++;
                    }
                }
                while (valid >= need)
                {
                    len = j - i + 1;
                    if (len < minLen)
                    {
                        minLen = len;
                        end = j;
                        start = i;
                    }
                    if (hash_t.find(s[i]) == hash_t.end())
                    {
                        i ++;
                    }
                    else
                    {
                        hash_t[s[i]] ++;
                        if (hash_t[s[i]] > 0)
                        {
                            valid --;
                        }
                        i ++;
                    }
                }
            }
            return (start == -1 || end == -1) ? "" : s.substr(start, minLen);
        }
    
    };
// @lc code=end