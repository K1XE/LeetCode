/*
 * @lc app=leetcode.cn id=2081 lang=cpp
 *
 * [2081] k 镜像数字的和
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
    long long kMirror(int k, int n) {
        auto check = [&](ll x) -> bool {
            V<int> digs;
            while (x) {
                digs.pb(x % k);
                x /= k;
            }
            for (int i = 0, j = digs.size() - 1; i < j; ++i, --j)
                if (digs[i] != digs[j]) return false;
            return true;
        };
        V<ll> res;
        res.reserve(n);
        __int128 p10[20];
        p10[0] = 1;
        for (int i = 1; i < 20; ++i) p10[i] = p10[i-1] * 10;
        for (int len = 1; res.size() < n; ++len) {
            bool odd = (len % 2 != 0);
            int half = (len + 1) / 2;
            ll start = (half == 1 ? 1 : (ll)p10[half - 1]);
            ll end   = (ll)p10[half] - 1;
            for (ll prefix = start; prefix <= end && res.size() < n; ++prefix) {
                ll p = prefix;
                ll t = odd ? (prefix / 10) : prefix;
                while (t > 0) {
                    p = p * 10 + (t % 10);
                    t /= 10;
                }
                if (check(p)) res.pb(p);
            }
        }
        return accumulate(ALL(res), 0LL);
    }
};
// @lc code=end

