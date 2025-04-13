/*
 * @lc app=leetcode.cn id=844 lang=cpp
 *
 * [844] 比较含退格的字符串
 */

// @lc code=start
class Solution {
    public:
        bool backspaceCompare(string s, string t) {
            int sp = s.size() - 1, tp = t.size() - 1;
            int cnts = 0, cntt = 0;
            while (sp >= 0 || tp >= 0)
            {
                while (sp >= 0)
                {
                    if (s[sp] == '#')
                    {
                        cnts ++, sp --;
                    }
                    else
                    {
                        if (cnts)
                        {
                            cnts --, sp --;
                        }
                        else break;
                    }
                }
                while (tp >= 0)
                {
                    if (t[tp] == '#')
                    {
                        cntt ++, tp --;
                    }
                    else
                    {
                        if (cntt)
                        {
                            cntt --, tp --;
                        }
                        else break;
                    }
                }
                if (sp >= 0 && tp >= 0)
                {
                    if (s[sp] == t[tp]) sp --, tp --;
                    else return 0;
                }
                else 
                {
                    if (sp >= 0 || tp >= 0) return 0;
                };
            }
            return 1;
        }
    };
// @lc code=end
class Solution {
    public:
        bool backspaceCompare(string s, string t) {
            int sp = 0, tp = 0, cnt = 0;
            string s1 = "", t1 = "";
            for (int i = 0; i < s.size(); i ++ )
            {
                if (s[i] != '#')
                {
                    s1.push_back(s[i]);
                }
                else
                {
                    if (!s1.empty()) s1.pop_back();
                }
            }
            for (int i = 0; i < t.size(); i ++ )
            {
                if (t[i] != '#')
                {
                    t1.push_back(t[i]);
                }
                else
                {
                    if (!t1.empty()) t1.pop_back();
                }
            }
            return s1 == t1 ? 1 : 0;
        }
    };
