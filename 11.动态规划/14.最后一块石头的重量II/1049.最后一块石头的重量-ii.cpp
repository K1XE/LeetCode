/*
 * @lc app=leetcode.cn id=1049 lang=cpp
 *
 * [1049] 最后一块石头的重量 II
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
    int lastStoneWeightII(vector<int>& stones) {
        int sums_ = 0;
        for (auto& x : stones) sums_ += x;
        int t = sums_ / 2;
        V<V<int>> dp(stones.size() + 1, V<int>(t + 1, 0));
        FOR(i, 1, stones.size() + 1) FOR(j, 1, t + 1) {
            dp[i][j] = dp[i - 1][j];
            if (j >= stones[i - 1]) dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1]);
        }
        return sums_ - 2 * dp[stones.size()][t];
    }
};
// @lc code=end

class Solution {
    public:
        int lastStoneWeightII(vector<int>& stones) {
            int sums_ = 0;
            for (auto& x : stones) sums_ += x;
            int t = sums_ / 2;
            V<int> dp(t + 1, 0);
            for (auto& x : stones) {
                for (int j = t; j >= x; j -- ) {
                    ckmax(dp[j], dp[j - x] + x);
                }
            }
            return sums_ - dp[t] - dp[t];
        }
    };