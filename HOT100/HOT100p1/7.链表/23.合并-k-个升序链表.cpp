/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并 K 个升序链表
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
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int k = lists.size();
        auto cmp = [](const ListNode* a, const ListNode* b)
        {
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> heap;
        for (auto l : lists)
        {
            if (l)
            {
                heap.emplace(l);
            }
        }
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        while (heap.size())
        {
            ListNode* node = heap.top();
            heap.pop();
            if (node->next) heap.emplace(node->next);
            cur->next = node;
            cur = cur->next;
        }
        return dummy->next;
    }
};
// @lc code=end

class Solution {
    public:
        ListNode* mergeKLists(vector<ListNode*>& lists) {
            int k = lists.size();
            ListNode* dummy = new ListNode(0);
            ListNode* cur = dummy;
            while (check(lists))
            {
                
                int minVal = INT_MAX;
                int minIdx = 0;
                for (int i = 0; i < k; i ++ )
                {
                    if (lists[i] && lists[i]->val < minVal)
                    {
                        minVal = lists[i]->val;
                        minIdx = i;
                    }
                }
                cur->next = lists[minIdx];
                lists[minIdx] = lists[minIdx]->next;
                cur = cur->next;
            }
            return dummy->next;
        }
    private:
        bool check (vector<ListNode*>& l)
        {
            for (int i = 0; i < l.size(); i ++ )
            {
                if (l[i]) return 1;
            }
            return 0;
        }
    };