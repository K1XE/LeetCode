/*
 * @lc app=leetcode.cn id=459 lang=cpp
 *
 * [459] 重复的子字符串
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        vector<int> next(s.size());
        get_next(s, next);
        int len = s.size();
        return (next[len - 1] != 0 && !(len % (len - next[len - 1]))) ? 1 : 0;
    }
private:
    void get_next(string& s, vector<int>& next)
    {
        int j = 0;
        next[0] = 0;
        for (int i = 1; i < s.size(); i ++ )
        {
            while (j > 0 && s[j] != s[i]) j = next[j - 1];
            if (s[j] == s[i]) j ++;
            next[i] = j;
        }
        return;
    }
};

// @lc code=end
class Solution {
    public:
        bool repeatedSubstringPattern(string s) {
            string ss = s + s;
            ss.erase(ss.begin()), ss.erase(ss.end() - 1);
            vector<int> next(s.size());
            get_next(s, next);
            int i = 0, j = 0;
            while (i < ss.size())
            {
                if (ss[i] == s[j])
                {
                    i ++, j ++;
                    if (j == s.size()) return 1;
                }
                else
                {
                    if (j > 0) j = next[j - 1];
                    else i ++;
                }
            }
            return 0;
        }
    private:
        void get_next(string& s, vector<int>& next)
        {
            int j = 0;
            next[0] = 0;
            for (int i = 1; i < s.size(); i ++ )
            {
                while (j > 0 && s[i] != s[j])
                {
                    j = next[j - 1];
                }
                if (s[i] == s[j]) j ++;
                next[i] = j;
            }
            return;
        }
    };
class Solution {
    public:
        bool repeatedSubstringPattern(string s) {
            string ss = s + s;
            ss.erase(ss.begin()), ss.erase(ss.end() - 1);
            return ss.find(s) == string::npos ? 0 : 1;
        }
    };
class Solution {
    public:
        bool repeatedSubstringPattern(string s) {
            int len = 1;
            if (s.size() == 1) return 0;
            while (len <= s.size() / 2)
            {
                string str1 = s;
                string str2 = s.substr(0, len);
                if (str1.size() % str2.size() != 0)
                {
                    len ++;
                    continue;
                }
                int i = 0, j = 0;
                while (i < str1.size() && str1[i] == str2[j])
                {
                    i ++, j ++;
                    if (j == str2.size()) j = 0;
                }
                if (i == str1.size()) return 1;
                len ++;
            }
            return 0;
        }
    };
