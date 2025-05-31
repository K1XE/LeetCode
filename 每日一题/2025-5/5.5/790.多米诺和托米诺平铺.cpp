/*
 * @lc app=leetcode.cn id=790 lang=cpp
 *
 * [790] 多米诺和托米诺平铺
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
using matrix = vector<vector<long long>>;
const int MOD = 1'000'000'007;
class Solution {
public:
    matrix mul(matrix& a, matrix& b)
    {
        int m = a.size(), n = b[0].size();
        matrix c = matrix(m, vector<long long>(n));
        for (int i = 0; i < m; i ++ )
        {
            for (int k = 0; k < a[i].size(); k ++ )
            {
                for (int j = 0; j < n; j ++ )
                {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }
    matrix pow_mul(matrix a, int n, matrix f)
    {
        matrix res = f;
        while (n)
        {
            if (n & 1)
            {
                res = this->mul(a, res);
            }
            a = this->mul(a, a);
            n >>= 1;
        }
        return res;
    }
    int numTilings(int n) {
        if (n == 1) return 1;
        matrix f2 = {{2}, {1}, {1}};
        matrix m = {{2, 0, 1}, {1, 0, 0}, {0, 1, 0}};
        return this->pow_mul(m, n - 2, f2)[0][0];
    }
};
// @lc code=end

