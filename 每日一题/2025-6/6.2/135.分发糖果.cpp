/*
 * @lc app=leetcode.cn id=135 lang=cpp
 *
 * [135] 分发糖果
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
#define Rep(i, _) for (int i = (_) - 1; i >= 0; --i)
#define REP(i, _, __) for (int i = (__) - 1, i##end = _; i >= i##end; --i)
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
    int candy(vector<int> &r)
    {
        int n = r.size();
        if (n == 1) return 1;
        V<int> pack(n, 1);
        FOR(i, 1, n){
            if (r[i] > r[i - 1]) pack[i] = pack[i - 1] + 1;
        }
        int res = pack[n - 1];
        Rep(i, n - 1){
            if (r[i] > r[i + 1]) pack[i] = max(pack[i], pack[i + 1] + 1);
            res += pack[i];
        }
        return res;
    }
};
// @lc code=end
class Solution
{
public:
    int candy(vector<int> &ratings)
    {
        int n = ratings.size();
        if (n == 1) return 1;
        V<int> l(n, 1);
        FOR(i, 1, n){
            if (ratings[i] > ratings[i - 1]) l[i] = l[i - 1] + 1;
        }
        V<int> r(n, 1);
        r[n - 1] = l[n - 1];
        Rep(i, n - 1){
            if (ratings[i] > ratings[i + 1]) r[i] = max(l[i], r[i + 1] + 1);
        }
        int res = 0;
        For(i, n){
            res += max(r[i], l[i]);
        }
        return res;
    }
};