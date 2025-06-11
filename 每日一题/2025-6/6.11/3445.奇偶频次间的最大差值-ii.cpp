/*
 * @lc app=leetcode.cn id=3445 lang=cpp
 *
 * [3445] 奇偶频次间的最大差值 II
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
        int maxDifference(string s, int k) {
            const int inf = INT_MAX / 2;
            int ans = -inf;
            for (int x = 0; x < 5; x++) {
                for (int y = 0; y < 5; y++) {
                    if (y == x) {
                        continue;
                    }
                    int cur_s[5]{}, pre_s[5]{};
                    int min_s[2][2] = {{inf, inf}, {inf, inf}};
                    int left = 0;
                    for (int i = 0; i < s.size(); i++) {
                        cur_s[s[i] - '0']++;
                        int r = i + 1;
                        while (r - left >= k && cur_s[x] > pre_s[x] && cur_s[y] > pre_s[y]) {
                            int& p = min_s[pre_s[x] & 1][pre_s[y] & 1];
                            p = min(p, pre_s[x] - pre_s[y]);
                            pre_s[s[left] - '0']++;
                            left++;
                        }
                        ans = max(ans, cur_s[x] - cur_s[y] - min_s[cur_s[x] & 1 ^ 1][cur_s[y] & 1]);
                    }
                }
            }
            return ans;
        }
    };
    
// @lc code=end

