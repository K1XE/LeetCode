/*
 * @lc app=leetcode.cn id=211 lang=cpp
 *
 * [211] 添加与搜索单词 - 数据结构设计
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
    unordered_map<char, Node*> hash;
    bool end;
};

class WordDictionary {
public:
    Node *root = new Node();
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        Node *cur = root;
        for (auto& ch : word) {
            if (! cur->hash.contains(ch)) cur->hash[ch] = new Node();
            cur = cur->hash[ch];
        }
        cur->end = 1;
    }
    
    bool search(string word) {
        return dfs(0, word, root);
    }
    bool dfs(int idx, string s, Node* cur) {
        if (idx == s.size()) return cur->end;
        if (s[idx] == '.') {
            for (auto& [k, v] : cur->hash) {
                if(dfs(idx + 1, s, v)) return 1;
            }
            return 0;
        }
        else {
            if (! cur->hash.contains(s[idx])) return 0;
            else return dfs(idx + 1, s, cur->hash[s[idx]]);
        }
        return 1;
    } 
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
// @lc code=end

