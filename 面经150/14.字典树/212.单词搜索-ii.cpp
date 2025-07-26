/*
 * @lc app=leetcode.cn id=212 lang=cpp
 *
 * [212] 单词搜索 II
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

struct Node
{
    bool end = 0;
    string word = "";
    unordered_map<char, Node*> son;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Node* root = new Node();
        for (auto& w : words) {
            Node* cur = root;
            for (auto& ch : w) {
                if (! cur->son.contains(ch)) cur->son[ch] = new Node();
                cur = cur->son[ch];
            }
            cur->end = 1, cur->word = w;
        }
        unordered_set<string> res;
        int m = board.size(), n = board[0].size();
        auto dfs = [&] (this auto&& dfs, int x, int y, Node* root) -> void {
            char ch = board[x][y];
            Node* cur = root->son[ch];
            board[x][y] = '#';
            if (cur->end) res.insert(cur->word);
            for (auto& [dx, dy] : dir) {
                int nx = x + dx, ny = y + dy;
                if (0 <= nx && nx < m && 0 <= ny && ny < n && board[nx][ny] != '#' && cur->son.contains(board[nx][ny])) dfs(nx, ny, cur);
            }
            board[x][y] = ch;
        };
        FOR(i, 0, m) FOR(j, 0, n) if (root->son.contains(board[i][j])) dfs(i, j, root);
        return V<string> {ALL(res)};
    }
};
// @lc code=end

