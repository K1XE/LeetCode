/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
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
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, V<string>> hash;
        V<V<string>> res;
        for (auto& s : strs) {
            string t = s;
            ranges::sort(t);
            hash[t].pb(s);
        }
        for (auto& [_, val] : hash) res.eb(val);
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string, int> hash;
            V<V<string>> res;
            int idx = 0;
            for (auto& str : strs) {
                string tmp = str;
                ranges::sort(str);
                if (! hash.contains(str)) hash[str] = idx ++;
                if (hash[str] >= res.size()) res.emplace_back();
                res[hash[str]].pb(tmp);
            }
            return res;
        }
    };

class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            unordered_map<string, int> hash;
            int idx = 0;
            for (auto str : strs) {
                ranges::sort(str);
                if (! hash.contains(str)) hash[str] = idx ++;
            }
            V<V<string>> res(idx);
            for (auto& str: strs) {
                string tmp = str;
                ranges::sort(str);
                res[hash[str]].pb(tmp);
            }
            return res;
        }
    };
