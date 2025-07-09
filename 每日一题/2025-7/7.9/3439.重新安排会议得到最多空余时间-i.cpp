/*
 * @lc app=leetcode.cn id=3439 lang=cpp
 *
 * [3439] 重新安排会议得到最多空余时间 I
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
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        V<int> free(n + 1, 0);
        free[0] = startTime[0];
        FOR(i, 1, n) free[i] = startTime[i] - endTime[i - 1];
        free[n] = eventTime - endTime[n - 1];
        int sums_ = 0, res = 0;
        FOR(i, 0, n + 1) {
            sums_ += free[i];
            if (i < k) continue;
            ckmax(res, sums_);
            sums_ -= free[i - k];
        }
        return res;
    }
};
// @lc code=end

