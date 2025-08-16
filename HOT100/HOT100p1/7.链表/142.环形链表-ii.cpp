/*
 * @lc app=leetcode.cn id=142 lang=cpp
 *
 * [142] 环形链表 II
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct ListNode
{
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
            if (fast && fast->next)
            {
                fast = fast->next->next;
                slow = slow->next;
            }
            else return NULL;
            if (fast == slow) break;
        }
        ListNode* p = head;
        while (p != slow)
        {
            p = p->next;
            slow = slow->next;
        }
        return p;
    }
};
// @lc code=end

