/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
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
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> ss(ALL(nums));
        int res = 0;
        for (auto& x : nums) {
            if (! ss.contains(x)) continue;
            ss.erase(x);
            int l = x - 1, r = x + 1;
            while (ss.contains(l)) ss.erase(l --);
            while (ss.contains(r)) ss.erase(r ++);
            ckmax(res, r - l - 1);
        }
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_map<int, int> hash;
            for (auto& x : nums) hash[x] = 0;
            int res = 0;
            for (auto x : nums) {
                if (hash[x]) continue;
                int tmp = 1;
                hash[x] = 1;
                if (! hash.contains(x - 1)) while (hash.contains(x + 1)) tmp ++, x ++, hash[x] = 1;
                ckmax(res, tmp);
            }
            return res;
        }
    };