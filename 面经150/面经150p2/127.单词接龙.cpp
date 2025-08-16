/*
 * @lc app=leetcode.cn id=127 lang=cpp
 *
 * [127] 单词接龙
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
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        bool f = 0;
        for (auto& w : wordList) {
            if (endWord == w) {
                f = 1;
                break;
            }
        }
        if (! f) return 0;
        unordered_map<string, V<string>> hash;
        int n = beginWord.size();
        for (auto& w : wordList) {
            FOR(i, 0, n) {
                string s = w.substr(0, i) + "*" + w.substr(i + 1, n - i - 1);
                hash[s].pb(w);
            }
        }
        unordered_set<string> bss, ess, vis;
        int res = 1;
        bss.insert(beginWord), ess.insert(endWord);
        while (bss.size() && ess.size()) {
            if (bss.size() > ess.size()) swap(bss, ess);
            unordered_set<string> nxt;
            for (auto& w : bss) {
                FOR(i, 0, n) {
                    string s = w.substr(0, i) + "*" + w.substr(i + 1, n - i - 1);
                    for (auto& tmp : hash[s]) {
                        if (ess.contains(tmp)) return res + 1;
                        if (! vis.contains(tmp)) vis.insert(tmp), nxt.insert(tmp);
                    }
                }
            }
            bss = nxt;
            res ++;
        }
        return 0;
    }
};
// @lc code=end

