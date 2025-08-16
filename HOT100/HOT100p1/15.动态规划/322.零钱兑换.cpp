/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
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
#define REP(i, _, __) for (int i = (__), i##end = _; i >= i##end; --i)
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
    int coinChange(vector<int>& coins, int amount) {
        V<int> dp(amount + 1, inf);
        dp[0] = 0;
        For(i, coins.size()) For(j, amount + 1) {
            if (j >= coins[i]) ckmin(dp[j], dp[j - coins[i]] + 1);
        }
        return dp[amount] == inf ? -1 : dp[amount];
    }
};
// @lc code=end

class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            int cl = coins.size();
            V<V<int>> dp(cl + 1, V<int>(amount + 1, inf));
            dp[0][0] = 0;
            For(i, cl) For(j, amount + 1) {
                dp[i + 1][j] = dp[i][j];
                if (j >= coins[i]) ckmin(dp[i + 1][j], dp[i + 1][j - coins[i]] + 1);
            }
            return dp[cl][amount] == inf ? -1 : dp[cl][amount];
        }
    };