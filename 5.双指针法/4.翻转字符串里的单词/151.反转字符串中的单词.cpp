/*
 * @lc app=leetcode.cn id=151 lang=cpp
 *
 * [151] 反转字符串中的单词
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string reverseWords(string s) {
        delSpace(s);
        reverseString(s, 0, s.size() - 1);
        int i = 0, start = 0;
        while (i <= s.size())
        {
            if (i == s.size() || s[i] == ' ')
            {
                reverseString(s, start, i - 1);
                start = i + 1;
            }
            i ++;
        }
        return s;
    }
private:
    void reverseString(string& s, int l, int r)
    {
        while (l < r)
        {
            swap(s[l ++], s[r --]);
        }
    }
    void delSpace(string& s)
    {
        int slow = 0;
        for (int j = 0; j < s.size(); j ++ )
        {
            if (s[j] != ' ')
            {
                if (slow > 0) s[slow ++] = ' ';
                while (j < s.size() && s[j] != ' ')
                    s[slow ++] = s[j ++]; 
            }
        }
        s.resize(slow);
    }
};
// @lc code=end
class Solution {
    public:
        string reverseWords(string s) {
            int j = s.size() - 1;
            string res;
            while (j >= 0)
            {
                while (j >= 0 && s[j] == ' ') j --;
                string s1;
                while (j >= 0 && s[j] != ' ') s1 += s[j --];
                reverse(s1.begin(), s1.end());
                if (s1.size()) s1 += ' ';
                res += s1;
            }
            res.pop_back();
            return res;
        }
    };
