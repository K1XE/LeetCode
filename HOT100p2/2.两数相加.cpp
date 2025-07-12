/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x, ListNode* nxt) : val(x), next(nxt) {};
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sums_ = 0;
        int res = 0;
        int power = 0;
        ListNode *dummy = new ListNode(0, nullptr);
        ListNode *cur = dummy;
        while (l1 || l2 || sums_) {
            if (l1 && l2) sums_ += l1->val + l2->val;
            else if (l1 || l2) sums_ += l1 ? l1->val : l2->val;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
            cur->next = new ListNode(sums_ % 10, nullptr);
            cur = cur->next;
            sums_ /= 10;
        }
        return dummy->next;
    }
};
// @lc code=end

