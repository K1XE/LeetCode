/*
 * @lc app=leetcode.cn id=3405 lang=cpp
 *
 * [3405] 统计恰好有 K 个相等相邻元素的数组数目
 */

// @lc code=start
#pragma once
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#define ALL(v) v.begin(), v.end()
#define For(i, _) for (int i = 0, i##end = _; i < i##end; ++i)
#define FOR(i, _, __) for (int i = _, i##end = __; i < i##end; ++i)
#define Rep(i, _) for (int i = (_); i >= 0; --i)
#define REP(i, __, _) for (int i = (__), i##end = _; i >= i##end; --i)
typedef long long ll;
typedef unsigned long long ull;
#define V vector
#define pb push_back
#define pf push_front
#define qb pop_back
#define qf pop_front
#define eb emplace_back
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define fi first
#define se second
const int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
const int inf = 0x3f3f3f3f;
const ll infl = 0x3f3f3f3f3f3f3f3fll;
const int mod = 1e9 + 7;
template <class T>
inline bool ckmin(T &x, const T &y) { return x > y ? (x = y, true) : false; }
template <class T>
inline bool ckmax(T &x, const T &y) { return x < y ? (x = y, true) : false; }

const int MX = 100'000;
ll f[MX];
ll invf[MX];
ll qpow(ll x, int n) {
    ll res = 1;
    for (; n; n /= 2) {if (n % 2) res = res * x % mod; x = x * x % mod;}
    return res;
}
auto init = [] {
    f[0] = 1;
    FOR(i, 1, MX) f[i] = f[i - 1] * i % mod;
    invf[MX - 1] = qpow(f[MX - 1], mod - 2);
    REP(i, MX - 1, 1) invf[i - 1] = invf[i] * i % mod;
    return 0;
} ();
ll comb(int n, int m) {return f[n] * invf[m] % mod * invf[n - m] % mod;}
class Solution
{
public:
    int countGoodArrays(int n, int m, int k)
    {
        return m * comb(n - 1, k) % mod * qpow(m - 1, n - k - 1) % mod;
    }
};
// @lc code=end

class Solution
{
public:
    int countGoodArrays(int n, int m, int k)
    {
        V<V<int>> dp(n + 1, V<int>(k + 2, 0));
        dp[1][0] = m;
        FOR(i, 2, n + 1)
        FOR(j, 0, k + 1)
        {
            dp[i][j] = (1LL * dp[i - 1][j] * (m - 1)) % mod;
            if (j > 0)
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod;
        }
        return dp[n][k];
    }
};

class Solution
{
public:
    int countGoodArrays(int n, int m, int k)
    {
        V<int> prev(k + 2, 0), curr(k + 2, 0);
        prev[0] = m;
        FOR(i, 2, n + 1)
        {
            FOR(j, 0, k + 1)
            {
                curr[j] = (1LL * prev[j] * (m - 1)) % mod;
                if (j > 0)
                    curr[j] = (curr[j] + prev[j - 1]) % mod;
            }
            swap(curr, prev);
        }
        return prev[k];
    }
};