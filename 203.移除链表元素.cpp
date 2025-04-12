/*
 * @lc app=leetcode.cn id=203 lang=cpp
 *
 * [203] 移除链表元素
 */

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
        ListNode* removeElements(ListNode* head, int val) {
            ListNode* rh = new ListNode(-1);
            rh->next = head;
            ListNode* p = rh;
            ListNode* q = head;
            while (q)
            {
                if (q->val == val)
                {
                    p->next = q->next;
                }
                else
                {
                    p = q;
                }
                q = q->next;
            }
            return rh->next;
        }
    };
// @lc code=end

