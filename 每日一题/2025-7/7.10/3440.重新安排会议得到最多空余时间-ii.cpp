/*
 * @lc app=leetcode.cn id=3440 lang=cpp
 *
 * [3440] 重新安排会议得到最多空余时间 II
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
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        auto get = [&] (int i) -> int {
            if (i == 0) return startTime[0];
            if (i == n) return eventTime - endTime[n - 1];
            return startTime[i] - endTime[i - 1];
        };
        int a = 0, b = -1, c = -1;
        FOR(i, 1, n + 1) {
            int sz = get(i);
            if (sz > get(a)) {
                c = b; b = a; a = i;
            }
            else if (b < 0 || sz > get(b)) {
                c = b; b = i;
            }
            else if (c < 0 || sz > get(c)) {
                c = i;
            }
        }
        int res = 0;
        FOR(i, 0, n) {
            int sz = endTime[i] - startTime[i];
            if (i != a && i + 1 != a && sz <= get(a) || i != b && i + 1 != b && sz <= get(b) || sz <= get(c)) ckmax(res, get(i) + sz + get(i + 1));
            else ckmax(res, get(i) + get(i + 1));
        }
        return res;
    }
};
// @lc code=end

