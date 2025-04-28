/*
 * @lc app=leetcode.cn id=234 lang=cpp
 *
 * [234] 回文链表
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
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
    bool isPalindrome(ListNode* head) {
        ListNode* h1 = head;
        ListNode* h2 = head;
        int cnt = 0;
        while (head)
        {
            cnt ++;
            head = head->next;
        }
        if (cnt == 1) return 1;
        int b = cnt / 2;
        while (-- b)
        {
            h2 = h2->next;
        }
        if (cnt % 2) h2 = h2->next;
        ListNode* dummy = h2;
        h2 = h2->next;
        while (h2->next)
        {
            ListNode* tmp = h2->next;
            h2->next = tmp->next;
            tmp->next = dummy->next;
            dummy->next = tmp;
        }
        h2 = dummy->next;
        while (h2)
        {
            if (h1->val != h2->val) return 0;
            h2 = h2->next;
            h1 = h1->next;
        }
        return 1;
    }
};
// @lc code=end

