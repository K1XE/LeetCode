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
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next = head;
            ListNode* pre = dummyHead;
            ListNode* cur = head;
            while (cur)
            {
                if (cur->val == val)
                {
                    pre->next = cur->next;
                    cur = cur->next;
                }
                else
                {
                    pre = cur;
                    cur = cur->next;
                }
            }
            return dummyHead->next;
        }
    };
// @lc code=end

