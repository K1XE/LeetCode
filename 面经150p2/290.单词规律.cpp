/*
 * @lc app=leetcode.cn id=290 lang=cpp
 *
 * [290] 单词规律
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
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> hash1;
        unordered_map<string, char> hash2;
        int n = s.size();
        V<string> words;
        string ts = "";
        FOR(i, 0, n) {
            if (s[i] == ' ') words.pb(ts), ts = "";
            else ts += s[i];
        }
        words.pb(ts);
        if (pattern.size() != words.size()) return 0;
        n = pattern.size();
        FOR(i, 0, n) {
            if (hash1.contains(pattern[i]) && words[i] != hash1[pattern[i]]) return 0;
            else hash1[pattern[i]] = words[i];
            if (hash2.contains(words[i]) && hash2[words[i]] != pattern[i]) return 0;
            else hash2[words[i]] = pattern[i];
        }
        return 1;
    }
};
// @lc code=end

