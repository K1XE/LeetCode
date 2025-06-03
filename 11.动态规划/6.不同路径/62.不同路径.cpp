/*
 * @lc app=leetcode.cn id=62 lang=cpp
 *
 * [62] 不同路径
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
#define Rep(i, _) for (int i = (_) - 1; i >= 0; --i)
#define REP(i, _, __) for (int i = (__) - 1, i##end = _; i >= i##end; --i)
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
int init = []()
{ ios::sync_with_stdio(false); cin.tie(nullptr); return 0; }();

class Solution {
public:
    int uniquePaths(int m, int n) {
        V<V<int>> dp(m, V<int>(n, 1));
        FOR(i, 1, m) FOR(j, 1, n) dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        return dp[m - 1][n - 1];
    }
};
// @lc code=end

class Solution {
    public:
        int uniquePaths(int m, int n) {
            // 0 s 1 x 2 z 3 y
            V<V<V<ll>>> dp(m, V<V<ll>>(n, V<ll>(4, 0)));
            dp[0][0][0] = dp[0][0][2] = 1;
            For(i, m) For(j, n) {
                if (i - 1 >= 0) {
                    dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][2];
                } // s
                if (j - 1 >= 0) {
                    dp[i][j][2] += dp[i][j - 1][0] + dp[i][j - 1][2];
                } // z
            }
            return dp[m - 1][n - 1][0] + dp[m - 1][n - 1][2] >> 1;
        }
    };