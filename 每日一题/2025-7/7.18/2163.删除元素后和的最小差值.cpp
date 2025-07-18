/*
 * @lc app=leetcode.cn id=2163 lang=cpp
 *
 * [2163] 删除元素后和的最小差值
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
    long long minimumDifference(vector<int>& nums) {
        int m = nums.size();
        int n = m / 3;
        priority_queue<int, V<int>, greater<int>> hmin(nums.end() - n, nums.end());
        ll s = reduce(nums.end() - n, nums.end(), 0LL);
        V<ll> suf(m - n + 1);
        suf[m - n] = s;
        REP(i, m - n - 1, n) {
            int tmp = nums[i];
            if (tmp > hmin.top()) {
                s += tmp - hmin.top();
                hmin.push(tmp);
                hmin.pop();
            }
            suf[i] = s;
        }
        priority_queue<int> hmax(nums.begin(), nums.begin() + n);
        ll pre = reduce(nums.begin(), nums.begin() + n, 0LL);
        ll res = pre - suf[n];
        FOR(i, n, m - n) {
            int tmp = nums[i];
            if (tmp < hmax.top()) {
                pre += tmp - hmax.top();
                hmax.push(tmp);
                hmax.pop();
            }
            ckmin(res, pre - suf[i + 1]);
        }
        return res;
    }
};
// @lc code=end

