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
int m, n, res;

void dfs(V<V<int>>& g, V<V<bool>>& vis, int x, int y)
{
    vis[x][y] = 1;
    For(i, 4) {
        int nx = x + dir[i][0], ny = y + dir[i][1];
        if (nx < 0 || nx >= m || ny < 0 || ny >= n || g[nx][ny] == 0) res ++;
        if (0 <= nx && nx < m && 0 <= ny && ny < n && !vis[nx][ny] && g[nx][ny] == 1) dfs(g, vis, nx, ny);
    }
}

int main()
{
    cin >> m >> n;
    V<V<int>> g(m, V<int>(n));
    V<V<bool>> vis(m, V<bool>(n, 0));
    For(i, m) For(j, n) cin >> g[i][j];
    res = 0;
    For(i, m) For(j, n) {
        if (g[i][j] == 1 && !vis[i][j]) {
            dfs(g, vis, i, j);
            goto done;
        }
        
    }
done:
    cout << res << endl;
}