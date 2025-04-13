/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
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
        ListNode* swapPairs(ListNode* head) {
            ListNode* p = head;
            int cnt = 0;
            while (p)
            {
                cnt ++;
                p = p->next;
            }
            if (cnt == 0) return nullptr;
            if (cnt == 1) return head;
            int step = cnt / 2;
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next = head->next;
            ListNode* cur = head;
            ListNode* pre = new ListNode(0);
            pre->next = cur;
            ListNode* post = cur->next;
            while (step --)
            {
                pre->next = cur->next;
                cur->next = post->next;
                post->next = cur;
                if (!step) return dummyHead->next;
                pre = cur;
                cur = pre->next;
                post = cur->next;
            }
            return dummyHead->next;
        }
    };
// @lc code=end

