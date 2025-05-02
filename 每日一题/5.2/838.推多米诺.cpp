/*
 * @lc app=leetcode.cn id=838 lang=cpp
 *
 * [838] 推多米诺
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    string pushDominoes(string d) {
        d = 'L' + d + 'R';
        int pre = 0;
        for (int i = 1; i < d.size(); i ++ )
        {
            if (d[i] == '.') continue;
            if (d[i] == d[pre])
            {
                fill(d.begin() + pre + 1, d.begin() + i, d[i]);
            }
            else
            {
                if (d[i] == 'L')
                {
                    fill(d.begin() + pre + 1, d.begin() + (pre + i + 1) / 2, 'R');
                    fill(d.begin() + (i + pre) / 2 + 1, d.begin() + i, 'L');
                }
            }
            pre = i;
        }
        return d.substr(1, d.size() - 2);
    }
};
// @lc code=end

