/*
 * @lc app=leetcode.cn id=141 lang=cpp
 *
 * [141] 环形链表
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
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (1)
        {
            if (fast && fast->next)
            {
                fast = fast->next->next;
                slow = slow->next;
            }
            else return 0;
            if (slow == fast) break;
        }
        if (fast) return 1;
        else return 0;
    }
};
// @lc code=end

