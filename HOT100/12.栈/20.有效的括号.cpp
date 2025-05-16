/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> hash;
        stack<char> stk;
        hash['('] = ')', hash['['] = ']', hash['{'] = '}';
        for (auto ch : s)
        {
            if (hash.find(ch) != hash.end()) stk.push(ch);
            else if (ch == ')' || ch == ']' || ch == '}')
            {
                if (! stk.size() || hash[stk.top()] != ch) return 0;
                stk.pop();
            }
            else return 0;
        }
        return stk.empty();
    }
};
// @lc code=end

