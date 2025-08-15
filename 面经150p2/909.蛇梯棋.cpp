/*
 * @lc app=leetcode.cn id=909 lang=cpp
 *
 * [909] 蛇梯棋
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
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        auto get_xy = [&] (int pos) -> pii {
            int x =  n - (pos - 1) / n - 1;
            int y = (pos - 1) / n % 2 ? n - ((pos - 1) % n) - 1 : (pos - 1) % n;
            return {x, y};
        };
        queue<pii> q;
        unordered_set<int> vis;
        q.push({1, 0});
        vis.insert(1);
        while (q.size()) {
            auto [pos, step] = q.front(); q.pop();
            vis.insert(pos);
            if (pos >= n * n) return step;
            FOR(i, 1, 7) {
                int nxt = pos + i;
                if (nxt > n * n) continue;
                auto [nx, ny] = get_xy(nxt);
                if (board[nx][ny] != -1) nxt = board[nx][ny];
                if (! vis.contains(nxt)) vis.insert(nxt), q.push({nxt, step + 1});
            }
        }
        return -1;
    }
};
// @lc code=end

