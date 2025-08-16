/*
 * @lc app=leetcode.cn id=30 lang=cpp
 *
 * [30] 串联所有单词的子串
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
    vector<int> findSubstring(string s, vector<string>& words) {
        int n = s.size();
        int idx = 0;
        int sz = words[0].size();
        int sz_total = sz * words.size();
        V<int> res;
        unordered_map<string, int> hash;
        for (auto& w : words) hash[w] ++;
        FOR(i, 0, min(sz, n)) {
            int v = i;
            unordered_map<string, int> tmp;
            while (v + sz_total <= n) {
                if (v == i) {
                    int u = i;
                    while (u < v + sz_total) {
                        tmp[s.substr(u, sz)] += 1;
                        u += sz;
                    }
                }
                else {
                    string l = s.substr(v - sz, sz);
                    tmp[l] -= 1;
                    if (tmp[l] == 0) tmp.erase(l);
                    string r = s.substr(v + sz_total - sz, sz);
                    tmp[r] += 1;
                }
                if (tmp == hash) res.pb(v);
                v += sz;
            }
        }
        return res;
    }
};
// @lc code=end

