/*
 * @lc app=leetcode.cn id=763 lang=cpp
 *
 * [763] 划分字母区间
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> hash;
        int n = s.size();
        for (int i = 0; i < n; i ++ )
        {
            hash[s[i]] = i;
        }
        int sta = 0, eds = 0;
        vector<int> res;
        for (int i = 0; i < n; i ++ )
        {
            eds = max(eds, hash[s[i]]);
            if (i == eds)
            {
                res.push_back(eds - sta + 1);
                sta = eds + 1;
            }
        }
        return res;
    }
};
// @lc code=end

