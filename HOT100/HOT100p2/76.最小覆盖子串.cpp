/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
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
    string minWindow(string s, string t) {
        unordered_map<char, int> hash;
        for (auto& ch : t) hash[ch] ++;
        int i = 0, n = s.size();
        int valid = 0, need = hash.size();
        int len = inf, sta = -1;
        FOR(j, 0, n) {
            if (hash.contains(s[j]) && -- hash[s[j]] == 0) valid ++;
            while (i <= j && valid == need) {
                if (j - i + 1 < len) sta = i, len = j - i + 1;
                if (hash.contains(s[i]) && ++ hash[s[i]] > 0) valid --;
                i ++;
            }
        }
        return sta == -1 ? "" : s.substr(sta, len); 
    }
};
// @lc code=end

class Solution {
    public:
        string minWindow(string s, string t) {
            unordered_map<char, int> hash;
            for (auto& ch : t) hash[ch] ++;
            int i = 0, n = s.size();
            int valid = 0, need = hash.size();
            int len = inf, sta = -1;
            FOR(j, 0, n) {
                if (hash.contains(s[j])) {
                    if (-- hash[s[j]] == 0) valid ++;
                }
                while (i <= j && valid == need) {
                    if (j - i + 1 < len) {
                        sta = i, len = j - i + 1;
                    }
                    if (hash.contains(s[i])) {
                        if (++ hash[s[i]] > 0) valid --;
                    }
                    i ++;
                }
            }
            return sta == -1 ? "" : s.substr(sta, len); 
        }
    };