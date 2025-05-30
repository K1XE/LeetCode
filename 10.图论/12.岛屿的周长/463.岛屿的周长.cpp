/*
 * @lc app=leetcode.cn id=463 lang=cpp
 *
 * [463] 岛屿的周长
 */
#include "tools.h"
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

class Solution
{
public:
    int res = 0;
    int islandPerimeter(vector<vector<int>> &g)
    {
        int m = g.size(), n = g[0].size();
        V<V<bool>> vis(m, V<bool>(n, 0));
        auto dfs = [&](auto &&self, int x, int y) -> void {
            vis[x][y] = 1;
            For(i, 4) {
                int nx = x + dir[i][0], ny = y + dir[i][1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || g[nx][ny] == 0)
                {
                    res ++;
                }
                else if (!vis[nx][ny]) self(self, nx, ny);
            }
        };
        For(i, m) For(j, n) {
            if (g[i][j] && !vis[i][j])
            {
                dfs(dfs, i, j);
                return res;
            }
        }
        return 123;
    };
};
// @lc code=end
