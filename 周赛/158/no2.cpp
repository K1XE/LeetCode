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
class Solution
{
public:
    long long maximumProfit(vector<int> &prices, int k)
    {
        int n_ = prices.size();
        ckmin(k, n_ / 2);
        V<V<array<ll, 3>>> dp(2, V<array<ll, 3>>(k + 1, {-infl, -infl, -infl}));
        For(j, k + 1) dp[0][j][0] = 0;
        int day = 0;
        For(i, n_) {
            int day_ = day ^ 1;
            For(j, k + 1) dp[day_][j][0] = dp[day_][j][1] = dp[day_][j][2] = -infl;
            For(j, k + 1) { 
                if (dp[day][j][0] != -infl) { // 0
                    ckmax(dp[day_][j][0], dp[day][j][0]);
                    if (j < k) {
                        ckmax(dp[day_][j][1], dp[day][j][0] - prices[i]);
                        ckmax(dp[day_][j][2], dp[day][j][0] + prices[i]);
                    }
                }
                if (dp[day][j][1] != -infl) { // 1
                    ckmax(dp[day_][j][1], dp[day][j][1]);
                    if (j < k) {
                        ckmax(dp[day_][j + 1][0], dp[day][j][1] + prices[i]);
                    }
                }
                if (dp[day][j][2] != -infl) {
                    ckmax(dp[day_][j][2], dp[day][j][2]);
                    if (j < k) {
                        ckmax(dp[day_][j + 1][0], dp[day][j][2] - prices[i]);
                    }
                }
            }
            day = day_;
        }
        return dp[day][k][0];
    }
};
