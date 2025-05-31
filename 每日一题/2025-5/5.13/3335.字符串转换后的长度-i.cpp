/*
 * @lc app=leetcode.cn id=3335 lang=cpp
 *
 * [3335] 字符串转换后的长度 I
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    const int MOD = 1'000'000'007;
    int lengthAfterTransformations(string s, int t) {
        vector<int> cur(26, 0);
        for (auto ch : s)
        {
            cur[ch - 'a'] += 1;
        }

        while (t --)
        {
            vector<int> nxt(26, 0);
            nxt[0] = cur[25];
            nxt[1] = (cur[25] + cur[0]) % MOD;
            for (int i = 2; i < 26; i ++ ) nxt[i] = cur[i - 1];
            cur = nxt;
        }
        long long res = 0;
        for (int i = 0; i < 26; i ++ )
        {
            res = (res + cur[i]) % MOD;
        }
        return res;
    }
};
// @lc code=end

