/*
 * @lc app=leetcode.cn id=1047 lang=cpp
 *
 * [1047] 删除字符串中的所有相邻重复项
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;

// @lc code=start
class Solution {
public:
    string removeDuplicates(string s) {
        string stk;
        for (int i = 0; i < s.size(); i ++ )
        {
            if (stk.size() && s[i] == stk.back()) stk.pop_back();
            else stk.push_back(s[i]);
        }
        return stk;
    }
};
// @lc code=end

