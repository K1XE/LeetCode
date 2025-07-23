/*
 * @lc app=leetcode.cn id=1717 lang=cpp
 *
 * [1717] 删除子字符串的最大得分
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
    int maximumGain(string s, int x, int y) {
        int n = s.size();
        if (x < y) {
            swap(x, y);
            FOR(i, 0, n) {
                if (s[i] == 'a') s[i] = 'b';
                else if (s[i] == 'b') s[i] = 'a';
            }
        }
        int i = 0, res = 0;
        while (i < n) {
            while (i < n && s[i] != 'a' && s[i] != 'b') i ++;
            int ca = 0, cb = 0;
            while (i < n && (s[i] == 'a' || s[i] == 'b')) {
                if (s[i] == 'a') {
                    ca ++;
                }
                else {
                    if (ca > 0) {
                        res += x;
                        ca --;
                    }
                    else cb ++;
                }
                i ++;
            }
            res += min(ca, cb) * y;
        }
        return res;
    }
};
// @lc code=end

