/*
 * @lc app=leetcode.cn id=123 lang=cpp
 *
 * [123] 买卖股票的最佳时机 III
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
int init = []()
{ ios::sync_with_stdio(false); cin.tie(nullptr); return 0; }();
/* 0 : begin
1 : buy1
2 : send1
3 : buy2
4: send2 */
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        V<V<int>> dp(n + 1, V<int>(5, -inf));
        dp[0][0] = 0;
        FOR(i, 1, n + 1) {
            dp[i][0] = dp[i - 1][0];
            dp[i][1] = max(dp[i - 1][0] - prices[i - 1], dp[i - 1][1]);
            dp[i][2] = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][2]);
            dp[i][3] = max(dp[i - 1][2] - prices[i - 1], dp[i - 1][3]);
            dp[i][4] = max(dp[i - 1][3] + prices[i - 1], dp[i - 1][4]);
        }
        int res = -inf;
        FOR(i, 0, 5) ckmax(res, dp[n][i]);
        return res;
    }
};
// @lc code=end

