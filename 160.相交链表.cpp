/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 class Solution {
    public:
        ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
            ListNode* p = headA;
            ListNode* q = headB;
            int cntp = 0, cntq = 0;
            while (p)
            {
                cntp ++;
                p = p->next;
            }
            while (q)
            {
                cntq ++;
                q = q->next;
            }
            p = headA, q= headB;
            if (cntp > cntq)
            {
                int diff = cntp - cntq;
                while (diff --)
                {
                    p = p->next;
                }
            }
            if (cntp < cntq)
            {
                int diff = cntq - cntp;
                while (diff --)
                {
                    q = q->next;
                }
            }
            while(q && p)
            {
                if (p == q) return p;
                p = p->next, q = q->next;
            }
            return nullptr;
        }
    };
// @lc code=end

