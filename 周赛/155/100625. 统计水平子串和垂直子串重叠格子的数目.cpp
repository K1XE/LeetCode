#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        int countCells(vector<vector<char>>& grid, string pattern) {
            int m = grid.size(), n = grid[0].size();
            vector<vector<int>> map(m, vector<int>(n, 0));
            for (int i = 0; i < m; i ++ )
            {
                for (int j = 0; j < n; j ++ )
                {
                    map[i][j] = 0;
                }
            }
            string sl;
            for (int j = 0; j < n; j ++ )
            {
                for (int i = 0; i < m; i ++ )
                {
                    sl += grid[i][j];
                }
            }
            string sh;
            for (int i = 0; i < m; i ++ )
            {
                for (int j = 0; j < n; j ++ )
                {
                    sh += grid[i][j];
                }
            }
            vector<int> diffl(m * n + 1), diffh(m * n + 1);
            bool bl = isSubstr(sl, pattern, diffl);
            bool bh = isSubstr(sh, pattern, diffh);
            int a = 0;
            for (int i = 0; i < diffl.size(); i ++ )
            {
                a += diffl[i];
                if (a > 0)
                {
                    map[i % m][i / m] |= 1;
                }
            }
            for (int i = 0; i < diffh.size(); i ++ )
            {
                a += diffh[i];
                if (a > 0)
                {
                    map[i / n][i % n] |= 2;
                }
            }
            int res = 0;
            for (int i = 0; i < m; i ++ )
            {
                for (int j = 0; j < n; j ++ )
                {
                    if ((map[i][j] & 1) && (map[i][j] & 2)) res ++;
                }
            }
            return res;
        }
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
        bool isSubstr(string s, string t, vector<int>& diff)
        {
            vector<int> next(t.size());
            getNext(t, next);
            int i = 0, j = 0;
            while (i < s.size())
            {
                if (s[i] == t[j])
                {
                    i ++, j ++;
                    if (j == t.size())
                    {
                        int tmp = i - j;
                        diff[tmp] ++;
                        diff[tmp + t.size()] --;
                        j = next[j - 1];
                    }
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