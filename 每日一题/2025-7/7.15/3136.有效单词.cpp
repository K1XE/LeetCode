/*
 * @lc app=leetcode.cn id=3136 lang=cpp
 *
 * [3136] 有效单词
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
    bool isValid(string word) {
        if (word.size() < 3) return 0;
        auto isVovel = [&] (char ch) -> bool {
            ch = tolower(ch);
            return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
        };
        bool b1 = 0, b2 = 0;
        for (auto& ch : word) {
            if (!isalnum(ch)) return 0;
            if (isalpha(ch)) {
                if (isVovel(ch)) b1 = 1;
                else b2 = 1;
            }
        }
        return b1 && b2;
    }
};
// @lc code=end

class Solution {
    public:
        bool isValid(string word) {
            auto isVovel = [&] (char ch) -> bool {
                return string("aeiou").find(tolower(ch)) != string::npos;
            };
            int n = word.size();
            if (n < 3) return 0;
            int ok = 0;
            bool b1 = 1, b2 = 1;
            unordered_set<char> ss;
            FOR(i, 0, 10) ss.insert(i + '0');
            for (char c = 'a'; c <= 'z'; c ++ ) ss.insert(c);
            for (char c = 'A'; c <= 'Z'; c ++ ) ss.insert(c);
            for (auto& ch : word) {
                if (!ss.contains(ch)) return 0;
                if (isVovel(ch) && b1) ok ++, b1 = 0;
                if (isalpha(ch) && !isVovel(ch) && b2) ok ++, b2 = 0;
            }
            return ok == 2;
        }
    };