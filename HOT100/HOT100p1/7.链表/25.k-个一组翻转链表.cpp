/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int back = k;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* starts = pre->next;
        ListNode* ends = starts;
        while (ends)
        {
            k --;
            ends = ends->next;
            if (! k)
            {
                reverseList(pre, starts, ends);
                k += back;
            }
        }
        return dummy->next;
    }
private:
    void reverseList(ListNode* &pre, ListNode* &starts, ListNode* &ends)
    {
        ListNode* u = starts;
        pre->next = ends;
        while (starts != ends)
        {
            ListNode* tmp = starts->next;
            starts->next = pre->next;
            pre->next = starts;
            starts = tmp;
        }
        pre = u;
        starts = ends;
    }
};
// @lc code=end

