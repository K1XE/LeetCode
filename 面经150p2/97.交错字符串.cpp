/*
 * @lc app=leetcode.cn id=97 lang=cpp
 *
 * [97] 交错字符串
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
    bool isInterleave(string s1, string s2, string s3) {
        int n1 = s1.size(), n2 = s2.size();
        if (n1 + n2 != s3.size()) return 0;
        V<V<bool>> dp(n1 + 1, V<bool>(n2 + 1, false));
        FOR(i, 1, n1 + 1) {
            if (s1[i - 1] != s3[i - 1]) break;
            dp[i][0] = 1;
        }
        FOR(j, 1, n2 + 1) {
            if (s2[j - 1] != s3[j - 1]) break;
            dp[0][j] = 1;
        }
        FOR(i, 1, n1 + 1) FOR(j, 1, n2 + 1) dp[i][j] = (dp[i - 1][j] & s1[i - 1] == s3[i + j - 1]) | 
                                                       (dp[i][j - 1] & s2[j - 1] == s3[i + j - 1]);
        return dp[n1][n2];
    }
};
// @lc code=end

