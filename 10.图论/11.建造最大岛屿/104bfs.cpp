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
int m, n, area;

void bfs(V<V<bool>>& vis, V<V<int>>& g, int x, int y, int mk)
{
    queue<pii> q;
    q.emplace(x, y);
    vis[x][y] = 1;
    g[x][y] = mk;
    area = 0;
    while (q.size())
    {
        auto [u, v] = q.front(); q.pop();
        area ++;
        For(i, 4) {
            int nx = u + dir[i][0], ny = v + dir[i][1];
            if (0 <= nx && nx < m && 0 <= ny && ny < n && g[nx][ny] == 1 && !vis[nx][ny]) {
                vis[nx][ny] = 1;
                g[nx][ny] = mk;
                q.emplace(nx, ny);
            }
        }
    }
}

int main()
{
    cin >> m >> n;
    V<V<int>> g(m, V<int>(n));
    For(i, m) For(j, n) cin >> g[i][j];
    int mk = 2;
    V<V<bool>> vis(m, V<bool>(n, 0));
    bool ff = 1;
    unordered_map<int, int> hash;
    For(i, m) For(j, n) {
        if (g[i][j] == 0) ff = 0;
        if (!vis[i][j] && g[i][j] == 1) {
            bfs(vis, g, i, j, mk);
            hash[mk ++] = area;
        }
    }
    if (ff) {
        cout << m * n << endl;
        return 0;
    }
    int res = 0;
    unordered_set<int> ss;
    For(i, m) {
        For(j, n) {
            if (g[i][j] == 0) {
                ss.clear();
                int cur = 1;
                For(k, 4) {
                    int ni = i + dir[k][0], nj = j + dir[k][1];
                    if (0 <= ni && ni < m && 0 <= nj && nj < n && g[ni][nj] > 1 && ss.insert(g[ni][nj]).second ) {
                        cur += hash[g[ni][nj]];
                    }
                }
                ckmax(res, cur);
            }
        }
    }
    cout << res;
}