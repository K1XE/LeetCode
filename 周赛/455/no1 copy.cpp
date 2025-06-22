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
class Solution
{
public:
    vector<int> findCoins(vector<int> &nw)
    {
        int n = nw.size();
        V<ll> w(n + 1);
        w[0] = 1;
        FOR(i, 1, n + 1) w[i] = nw[i - 1];
        V<int> res;
        while (1) {
            int c = -1;
            FOR(i, 1, n + 1) {
                if (w[i] != 0) {
                    c = i;
                    break;
                }
            }
            if (c == -1) break;
            if (w[c] != 1) return{};
            res.pb(c);
            V<ll> prev = w;
            FOR(i, c, n + 1) {
                w[i] -= prev[i - c];
                if (w[i] < 0) return {};
            }
        }
        FOR(i, 1, n + 1) if (w[i]) return {};
        return res;
    }
};