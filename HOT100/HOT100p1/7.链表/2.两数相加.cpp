/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
// @lc code=start
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
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        int a = 0;
        while (l1 || l2 || a)
        {
            int sums = a;
            if (l1) sums += l1->val, l1 = l1->next;
            if (l2) sums += l2->val, l2 = l2->next;
            cur->next = new ListNode(sums % 10);
            a = sums / 10;
            cur = cur->next;
        }
        return dummy->next;
    }
};
// @lc code=end

