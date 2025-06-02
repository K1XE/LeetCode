/*
 * @lc app=leetcode.cn id=685 lang=cpp
 *
 * [685] 冗余连接 II
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

struct DSU
{
    V<int> fa, sz;
    DSU(int n) : fa(n), sz(n, 1)
    {
        iota(ALL(fa), 0);
    }
    int find(int x)
    {
        return x == fa[x] ? x : fa[x] = find(fa[x]);
    }
    bool unite(int a, int b)
    {
        a = find(a);
        b = find(b);
        if (a == b)
            return 1;
        if (sz[a] < sz[b])
            swap(a, b);
        fa[b] = a;
        sz[a] += sz[b];
        return 1;
    }
    bool isSame(int a, int b)
    {
        return find(a) == find(b);
    }
    int size(int x)
    {
        return sz[find(x)];
    }
    void reset()
    {
        iota(ALL(fa), 0);
        fill(ALL(sz), 1);
    }
};
class Solution
{
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>> &edges)
    {
        int n = edges.size();
        V<int> ind(n + 1);
        For(i, n) {
            int u = edges[i][0], v = edges[i][1];
            ind[v] ++;
        }
        V<int> vec;
        Rep(i, n) {
            if (ind[edges[i][1]] == 2) vec.pb(i);
        }
        auto check1 = [&] (int e) -> bool {
            DSU dsu(n + 5);
            For(i, n) {
                if (i == e) continue;
                if (dsu.isSame(edges[i][0], edges[i][1])) return 0;
                dsu.unite(edges[i][0], edges[i][1]);
            }
            return 1;
        };
        if (vec.size() > 0) {
            if (check1(vec[0])) return edges[vec[0]];
            else return edges[vec[1]];
        }
        auto check2 = [&] () -> V<int> {
            DSU dsu(n + 5);
            For(i, n) {
                if (dsu.isSame(edges[i][0], edges[i][1])) return edges[i];
                dsu.unite(edges[i][0], edges[i][1]);
            }
            return {};
        };
        return check2();
    }
};
// @lc code=end
