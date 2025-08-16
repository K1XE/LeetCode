/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并 K 个升序链表
 */
#include "tools.h"
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
struct cmp
{
    bool operator()(ListNode* a, ListNode* b)
    {
        return a->val > b->val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, cmp> heap;
        int sz = lists.size();
        int cnt = 0;
        for (auto p : lists)
        {
            if (p == NULL)
            {
                cnt ++;
                continue;
            }
            heap.emplace(p);
        }
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        while (cnt < sz)
        {
            ListNode* tmp = heap.top();
            heap.pop();
            cur->next = tmp;
            cur = cur->next;
            tmp = tmp->next;
            if (! tmp) cnt ++;
            else heap.emplace(tmp);
        }
        return dummy->next;
    }
};
// @lc code=end

