/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
 */
struct ListNode {
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
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            ListNode* dummy = new ListNode(0);
            dummy->next = head;
            ListNode* fast = dummy;
            ListNode* slow = dummy;
            n += 1;
            while (n --)
            {
                fast = fast->next;
            }
            while (fast != nullptr)
            {
                slow = slow->next;
                fast = fast->next;
            }
            slow->next = slow->next->next;
            return dummy->next;
        }
    };
    
// @lc code=end
