/*
 * @lc app=leetcode.cn id=139 lang=cpp
 *
 * [139] 单词拆分
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

class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        int maxl = ranges::max(wordDict, {}, &string::size).size();
        unordered_set<string> words(ALL(wordDict));
        int n = s.size();
        V<bool> dp(n + 1);
        dp[0] = 1;
        FOR(i, 1, n + 1) {
            REP(j, i - 1, max(i - maxl, 0)) {
                if (dp[j] && words.count(s.substr(j, i - j))) {
                    dp[i] = 1;
                    break;
                }
            }
        }
        return dp[n];
    }
};
// @lc code=end
class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        int maxl = ranges::max(wordDict, {}, &string::size).size();
        unordered_set<string> words(ALL(wordDict));
        int n = s.size();
        V<int> memo(n + 1, -1);
        auto dfs = [&](auto &&dfs, int i) -> bool
        {
            if (i == 0)
                return 1;
            int &res = memo[i];
            if (res != -1)
                return res;
            REP(j, max(i - maxl, 0), i - 1)
            {
                if (words.count(s.substr(j, i - j)) && dfs(dfs, j))
                    return res = 1;
            }
            return res = 0;
        };
        return dfs(dfs, n);
    }
};