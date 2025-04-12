/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */
struct ListNode{
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
        ListNode* swapPairs(ListNode* head) {
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next = head;
            ListNode* pre = dummyHead;
            while (pre->next && pre->next->next)
            {
                ListNode* p = pre->next;
                ListNode* q = pre->next->next;
                p->next = q->next;
                q->next = p;
                pre->next = q;
                pre = p;
            }
            return dummyHead->next;
        }
    };
// @lc code=end

