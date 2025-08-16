/*
 * @lc app=leetcode.cn id=234 lang=cpp
 *
 * [234] 回文链表
 */
#include "tools.h"

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
        ListNode* p = head;
        ListNode* dummy = new ListNode(0);
        
        dummy->next = head;
        int cnt = 0;

        while (p)
        {
            cnt ++;
            p = p->next;
        }
        int half = cnt / 2;
        p = dummy;
        for (int i = 0; i < half; i ++ )
        {
            p = p->next;
        }

        ListNode* dummy2 = p;
        ListNode* q = dummy2->next;
        dummy2->next = NULL;
        while (q)
        {
            ListNode* tmp = q->next;
            q->next = dummy2->next;
            dummy2->next = q;
            q = tmp;
        }
        q = dummy2->next;
        p = dummy->next;
        while (half --)
        {
            if (p->val != q->val) return 0;
            p = p->next;
            q = q->next;
        }
        return 1;
    }
};
// @lc code=end

