/*
 * @lc app=leetcode.cn id=142 lang=cpp
 *
 * [142] 环形链表 II
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
        ListNode *detectCycle(ListNode *head) {
            unordered_map<ListNode*, int> hash;
            ListNode* p = head;
            while (p)
            {
                hash[p] ++;
                if (hash[p] >= 2)
                {
                    break;
                }
                p = p->next;
            }
            p = head;
            while (p)
            {
                if (hash[p] >= 2)
                {
                    return p;
                }
                p = p->next;
            }
            return nullptr;
        }
    };
// @lc code=end
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
        ListNode *detectCycle(ListNode *head) {
            unordered_map<ListNode*, int> hash;
            ListNode* p = head;
            while (p)
            {
                hash[p] ++;
                if (hash[p] >= 2)
                {
                    return p;
                }
                p = p->next;
            }
            return nullptr;
        }
    };
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
        ListNode *detectCycle(ListNode *head) {
            ListNode* slow = head;
            ListNode* fast = head;
            while (1)
            {
                if (fast == nullptr || fast->next == nullptr) return nullptr;
                slow = slow->next, fast = fast->next->next;
                if (slow == fast) break;
            }
            ListNode* p = head;
            while (1)
            {
                if (p == slow) return p;
                slow = slow->next, p = p->next;
            }
        }
    };