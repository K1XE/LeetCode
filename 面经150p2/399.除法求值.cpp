/*
 * @lc app=leetcode.cn id=399 lang=cpp
 *
 * [399] 除法求值
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
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        using PSD = pair<string, double>;
        unordered_map<string, V<PSD>> g;
        int n = equations.size();
        FOR(i, 0, n) {
            g[equations[i][0]].eb(equations[i][1], values[i]);
            g[equations[i][1]].eb(equations[i][0], 1.0 / values[i]);
        }
        V<double> res;
        auto dfs = [&] (this auto&& dfs, string sta, string eds, unordered_set<string> vis, double cur) -> double {
            if (sta == eds) return cur;
            vis.insert(sta);
            for (auto& [v, w] : g[sta]) {
                if (! vis.contains(v)) {
                    double x = dfs(v, eds, vis, cur * w);
                    if (x != -1.0) return x;
                }
            }
            return -1.0;
        };
        for (auto& q : queries) {
            string sta = q[0], eds = q[1];
            if (! g.contains(sta) || ! g.contains(eds)) res.pb(-1);
            else if (sta == eds) res.pb(1.0);
            else {
                unordered_set<string> vis;
                res.pb(dfs(sta, eds, vis, 1));
            } 
        }
        return res;
    }
};
// @lc code=end

