/*
 * @lc app=leetcode.cn id=2901 lang=cpp
 *
 * [2901] 最长相邻不相等子序列 II
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        auto check = [&](string& s1, string& s2, int idx1, int idx2) -> bool
        {
            if (groups[idx1] == groups[idx2]) return 0;
            if (s1.size() != s2.size()) return 0;
            int cnt = 0;
            for (int i = 0; i < s1.size(); i ++ )
            {
                if (s1[i] != s2[i]) cnt ++;
                if (cnt > 1) return 0;
            }
            return cnt == 1;
        };
        int n = words.size();
        vector<int> dp(n, 1), pre(n, -1);
        int maxl = 1, last = 0;
        for (int i = 0; i < n; i ++ )
        {
            for (int j = 0; j < i; j ++ )
            {
                if (check(words[j], words[i], j, i))
                {
                    if (dp[j] + 1 > dp[i])
                    {
                        dp[i] = dp[j] + 1;
                        pre[i] = j;
                    }
                }
            }
            if (dp[i] > maxl)
            {
                maxl = dp[i];
                last = i;
            }
        }
        vector<string> res;
        while (last != -1)
        {
            res.push_back(words[last]);
            last = pre[last];
        }
        ranges::reverse(res);
        return res;
    }
};
// @lc code=end

