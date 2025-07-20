/*
 * @lc app=leetcode.cn id=1948 lang=cpp
 *
 * [1948] 删除系统中的重复文件夹
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

struct TrieNode
{
    unordered_map<string, TrieNode*> son;
    string name;
    bool del_ = 0;
};

class Solution {
public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        TrieNode* root = new TrieNode();
        for (auto& p : paths) {
            TrieNode *cur = root;
            for (auto& s : p) {
                if (! cur->son.contains(s)) {
                    cur->son[s] = new TrieNode();
                }
                cur = cur->son[s];
                cur->name = s;
            }
        }
        unordered_map<string, TrieNode*> expr_to_node;
        auto gen_expr = [&] (this auto&& gen_expr, TrieNode* node) -> string {
            if (node->son.empty()) return node->name;
            V<string> expr;
            for (auto& [_, son] : node->son)
                expr.eb("(" + gen_expr(son) + ")");
            ranges::sort(expr);
            string sub_tree_expr;
            for (auto& e : expr) sub_tree_expr += e;
            if (expr_to_node.contains(sub_tree_expr)) {
                expr_to_node[sub_tree_expr]->del_ = 1;
                node->del_ = 1;
            }
            else {
                expr_to_node[sub_tree_expr] = node;
            }
            return node->name + sub_tree_expr;
        };
        for (auto& [_, son] : root->son) gen_expr(son);
        V<V<string>> res;
        V<string> path;
        auto dfs = [&] (this auto&& dfs, TrieNode* n) -> void {
            if (n->del_) return;
            path.pb(n->name);
            res.eb(path);
            for (auto& [_, son] : n->son) dfs(son);
            path.qb();
        };
        for (auto& [_, son] : root->son) dfs(son);
        return res;
    }
};
// @lc code=end

