/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU 缓存
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
    int key, val;
    Node *nxt;
    Node *pre;
    Node(int k, int v) : key(k), val(v), nxt(nullptr), pre(nullptr) {};
};
class LRUCache {
public:
    unordered_map<int, Node*> hash;
    Node *dummy = new Node(0, 0);
    int cnt = 0;
    void rm(Node *n) {
        Node *tmp = n->pre;
        tmp->nxt = n->nxt;
        n->nxt->pre = tmp;
    }
    void push_front(Node *n) {
        Node *tmp = n;
        if (n->nxt || n->pre) rm(n);
        tmp->nxt = dummy->nxt;
        dummy->nxt = tmp;
        tmp->nxt->pre = tmp;
        tmp->pre = dummy;
    }
    Node* get_node(int key) {
        if (hash.count(key)) {
            push_front(hash[key]);
            return hash[key];
        }
        return NULL;
    }
    LRUCache(int capacity) {
        dummy->nxt = dummy;
        dummy->pre = dummy;
        cnt = capacity;
    }

    int get(int key) {
        auto tmp = get_node(key);
        if (tmp) return tmp->val;
        return -1;
    }
    
    void put(int key, int value) {
        auto tmp = get_node(key);
        if (tmp) {
            tmp->val = value;
            return;
        }
        Node *n = new Node(key, value);
        hash[key] = n;
        push_front(n);
        if (! cnt --) {
            Node *tail = dummy->pre;
            rm(tail);
            hash.erase(tail->key);
            delete tail;
            cnt++;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

