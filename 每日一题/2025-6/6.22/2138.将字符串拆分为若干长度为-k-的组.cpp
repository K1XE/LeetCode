/*
 * @lc app=leetcode.cn id=2138 lang=cpp
 *
 * [2138] 将字符串拆分为若干长度为 k 的组
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
    vector<string> divideString(string s, int k, char fill) {
        V<string> res;
        int n = s.size();
        int idx = 0;
        while (idx < n) {
            if (idx + k - 1 >= n) break;
            string ss = "";
            FOR(j, idx, idx + k) ss.pb(s[j]);
            res.pb(ss);
            idx += k;
        }
        if (idx == n) return res;
        int cnt = 0;
        string ss = "";
        FOR(i, idx, n) ss.pb(s[i]), cnt ++;
        int t = k - cnt;
        while (t --) ss.pb(fill);
        res.pb(ss);
        return res;
    }
};
// @lc code=end

