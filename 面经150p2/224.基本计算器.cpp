/*
 * @lc app=leetcode.cn id=224 lang=cpp
 *
 * [224] 基本计算器
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
    int calculate(string s) {
        stack<int> stk;
        ll res = 0, x = 0, sign = 1;
        ll n = s.size(), idx = 0;
        while (idx < n) {
            if (isdigit(s[idx])) x = x * 10 + s[idx] - '0';
            else if (s[idx] == '+' || s[idx] == '-') {
                res += sign * x;
                x = 0;
                sign = s[idx] == '+' ? 1 : -1;
            }
            else if (s[idx] == '(') {
                stk.push(res);
                stk.push(sign);
                res = 0, sign = 1;
            }
            else if (s[idx] == ')') {
                ll ts = stk.top(); stk.pop();
                ll tx = stk.top(); stk.pop();
                res += sign * x;
                x = 0;
                res *= ts;
                res += tx;
            }
            idx ++;
        }
        return res + x * sign;
    }
};
// @lc code=end

