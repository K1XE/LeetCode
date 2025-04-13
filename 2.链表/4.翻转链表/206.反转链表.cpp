/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
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
        ListNode* reverseList(ListNode* head) {
            ListNode* dummyhead = new ListNode(0);
            dummyhead->next = head;
            ListNode* p = head;
            if (!p) return nullptr;
            while (p->next)
            {
                ListNode* t = new ListNode(0);
                t = p->next;
                p->next = t->next;
                t->next = dummyhead->next;
                dummyhead->next = t;
            }
            return dummyhead->next;
        }
    };
// @lc code=end

