/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并 K 个升序链表
 */
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {};
};
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

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [] (auto& a, auto& b) {
            return a->val > b->val;
        };
        priority_queue<ListNode*, V<ListNode*>, decltype(cmp)> h(cmp);
        int n = lists.size();
        FOR(i, 0, n) {
            if (lists[i]) h.emplace(lists[i]);
        }
        ListNode *dummy = new ListNode(0);
        ListNode *cur = dummy;
        while (h.size()) {
            auto tmp = h.top(); h.pop();
            cur->next = tmp;
            tmp = tmp->next;
            if (tmp) h.emplace(tmp);
            cur = cur->next;
        }
        return dummy->next;
    }
};
// @lc code=end

class Solution {
    public:
        ListNode* mergeKLists(vector<ListNode*>& lists) {
            using pLi = pair<ListNode*, int>;
            auto cmp = [](const pLi a, const pLi b) {
                return a.fi->val > b.fi->val;
            };
            priority_queue<pLi, V<pLi>, decltype(cmp)> h(cmp);
            int n = lists.size();
            FOR(i, 0, n) {
                if (lists[i]) h.emplace(lists[i], i);
            }
            ListNode *dummy = new ListNode(0);
            ListNode *cur = dummy;
            while (h.size()) {
                pLi tmp = h.top(); h.pop();
                cur->next = tmp.fi;
                tmp.fi = tmp.fi->next;
                if (tmp.fi) h.emplace(tmp.fi, tmp.se);
                cur = cur->next;
            }
            return dummy->next;
        }
    };