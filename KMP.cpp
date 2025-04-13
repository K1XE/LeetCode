#include <bits/stdc++.h>
using namespace std;
class KMP{
    public:
        void getNext(string& s, vector<int>& next)
        {
            int j = 0; // 前缀末尾
            next[0] = 0;
            for (int i = 1; i < s.size(); i ++ )
            {
                while (j > 0 && s[j] != s[i]) j = next[j - 1]; // 找到最长相同前后缀
                if (s[j] == s[i]) j ++; // 找到了相同前后缀
                next[i] = j; // 将前缀长度赋给next
            }
        }
        bool isSubstr(string s, string t)
        {
            vector<int> next(t.size());
            getNext(t, next);
            int i = 0, j = 0;
            while (i < s.size())
            {
                if (s[i] == s[j])
                {
                    i ++, j ++;
                    if (j == t.size()) return 1;
                }
                else
                {
                    if (j > 0) j = next[j - 1]; // 找t开始匹配的位置
                    else i ++; // 没有相同前后缀 i后移
                }
            }
            return 0;
        }
};