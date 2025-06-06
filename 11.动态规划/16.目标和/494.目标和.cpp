/*
 * @lc app=leetcode.cn id=494 lang=cpp
 *
 * [494] 目标和
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
#define REP(i, _, __) for (int i = (__), i##end = _; i >= i##end; --i)
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
    int findTargetSumWays(vector<int>& nums, int target) {
        int sums = accumulate(ALL(nums), 0);
        int t = sums + target >> 1;
        if ((sums + target) % 2 || abs(target) > sums) return 0;
        V<int> dp(t + 1);
        dp[0] = 1;
        for (auto& x : nums) {
            for (int i = t; i >= x; i -- ) {
                dp[i] += dp[i - x];
            }
        }
        return dp[t];
    }
};
// @lc code=end

class Solution {
    public:
        int findTargetSumWays(vector<int>& nums, int target) {
            int n = nums.size();
    
            unordered_map<string, int> memo;
    
            auto dfs = [&] (auto&& self, int sta, int sums) -> int
            {
                if (sta == n) return sums == target;
                string key = to_string(sta) + ',' + to_string(sums);
                if (memo.count(key)) return memo[key];
                int plus = self(self, sta + 1, sums + nums[sta]);
                int minus = self(self, sta + 1, sums - nums[sta]);
                return memo[key] = plus + minus;
            };
            return dfs(dfs, 0, 0);
        }
    };