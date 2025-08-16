/*
 * @lc app=leetcode.cn id=763 lang=cpp
 *
 * [763] 划分字母区间
 */
#include "tools.h"

// @lc code=start
class Solution
{
public:
    vector<int> partitionLabels(string s)
    {
        unordered_map<char, int> hash;
        int n = s.size();
        for (int i = 0; i < n; i++)
        {
            hash[s[i]] = i;
        }
        int end = 0, start = 0;
        vector<int> res;
        for (int i = 0; i < n; i++)
        {
            end = max(end, hash[s[i]]);
            if (i == end)
            {
                res.push_back(end - start + 1);
                start = end + 1;
            }
        }
        return res;
    }
};
// @lc code=end
