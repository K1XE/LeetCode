/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
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
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next = head;
            int cnt = 0;
            while (head)
            {
                cnt ++;
                head = head->next;
            }
            ListNode* p = dummyHead;
            int diff = cnt - n;
            while (diff --)
            {
                p = p->next;
            }
            if (p->next)
            {
                p->next = p->next->next;
            }
            else return nullptr;
            return dummyHead->next;
        }
    };
// @lc code=end
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
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next = head;
            ListNode* slow = dummyHead;
            ListNode* fast = dummyHead;
            while (n -- && fast)
            {
                fast = fast->next;
            }
            fast = fast->next;
            while (fast)
            {
                slow = slow->next, fast = fast->next;
            }
            slow->next = slow->next->next;
            return dummyHead->next;
            
        }
    };
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
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next = head;
            ListNode* slow = dummyHead;
            ListNode* fast = dummyHead;
            int step = n + 1;
            while (step --)
            {
                fast = fast->next;
                if (fast == nullptr) break;
            }
            while (fast)
            {
                slow = slow->next, fast = fast->next;
            }
            if (slow->next)
            {   
                slow->next = slow->next->next;
            }
            return dummyHead->next;
            
        }
    };