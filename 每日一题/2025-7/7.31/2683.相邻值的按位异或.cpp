/*
 * @lc app=leetcode.cn id=2683 lang=cpp
 *
 * [2683] 相邻值的按位异或
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
    bool doesValidArrayExist(vector<int>& derived) {
        int n = derived.size();
        int res = derived[0];
        FOR(i, 1, n) res ^= derived[i];
        return res == 0;
    }
};
// @lc code=end

class Solution {
    public:
        bool doesValidArrayExist(vector<int>& derived) {
            V<int> res;
            auto gen = [&] (int x) -> bool {
                res.clear();
                res.pb(x);
                int n = derived.size();
                FOR(i, 0, n) {
                    if (derived[i] == 0) {
                        if (res.back() == 0) res.pb(0);
                        else res.pb(1);
                    }
                    else {
                        if (res.back() == 0) res.pb(1);
                        else res.pb(0);
                    }
                }
                if (res.back() == res[0]) return 1;
                else return 0;
            };
            return gen(0) || gen(1);
        }
    };