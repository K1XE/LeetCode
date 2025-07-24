/*
 * @lc app=leetcode.cn id=2322 lang=cpp
 *
 * [2322] 从树中删除边的最小分数
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

class Solution {
public:
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        V<V<int>> g(n);
        for (auto& e : edges) {
            int x = e[0], y = e[1];
            g[x].pb(y), g[y].pb(x);
        }
        int clock = 0;
        V<int> xr(n), in(n), out(n);
        auto dfs = [&] (this auto&& dfs, int x, int fa) -> void {
            in[x] = ++ clock;
            xr[x] = nums[x];
            for (auto& y : g[x]) {
                if (y != fa) {
                    dfs(y, x);
                    xr[x] ^= xr[y];
                }
            }
            out[x] = clock;
        };
        dfs(0, -1);
        auto is_ancestor = [&] (int x, int y) -> bool {
            return in[x] < in[y] && in[y] <= out[x];
        };
        int res = inf;
        FOR(x, 2, n) FOR(y, 1, x) {
            int a, b, c;
            if (is_ancestor(x, y)) {
                a = xr[y], b = xr[x] ^ a, c = xr[0] ^ xr[x];
            }
            else if (is_ancestor(y, x)) {
                a = xr[x], b = xr[y] ^ a, c = xr[0] ^ xr[y];
            }
            else a = xr[x], b = xr[y], c = xr[0] ^ a ^ b;
            ckmin(res, max({a, b, c}) - min({a, b, c}));
            if (res == 0) return res;
        }
        return res;
    }
};
// @lc code=end

