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

V<int> path;
V<V<int>> res;

void dfs(int u, int n, V<V<int>>& g)
{
    
    path.pb(u);
    if (u == n) res.pb(path);
    else for(auto& v : g[u]) dfs(v, n, g);
    path.qb();
}

int main()
{
    int N, M; cin >> N >> M;
    V<V<int>> g(N + 1);
    For(i, M) {
        int u, v; cin >> u >> v;
        g[u].pb(v);
    }
    dfs(1, N, g);
    if (res.empty()) cout << -1 << "\n";
    else for (auto& p : res) {
        For(i, p.size()) cout << (i ? " " : "") << p[i];
        cout << "\n";
    }
}