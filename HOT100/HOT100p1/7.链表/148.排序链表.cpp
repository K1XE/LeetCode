/*
 * @lc app=leetcode.cn id=148 lang=cpp
 *
 * [148] 排序链表
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
    ListNode* sortList(ListNode* head) {
        int len = this->get_len(head);
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        for (int i = 1; i < len; i *= 2)
        {
            ListNode* new_list_tail = dummy;
            ListNode* cur = dummy->next;
            while (cur)
            {
                ListNode* head1 = cur;
                ListNode* head2 = this->split(head1, i);
                cur = this->split(head2, i);
                auto [head, tail] = merge(head1, head2);
                new_list_tail->next = head;
                new_list_tail = tail;
            }
        }
        return dummy->next;
    }
private:
    int get_len(ListNode* n)
    {
        int l = 0;
        while (n)
        {
            l ++;
            n = n->next;
        }
        return l;
    }
    ListNode* split(ListNode* &n, int size)
    {
        if (! n) return NULL;
        ListNode* cur = n;
        for (int i = 0; i < size - 1 && cur; i ++ )
        {
            cur = cur->next;
        }
        if (! cur || ! cur->next) return NULL;
        ListNode* next_head = cur->next;
        cur->next = NULL;
        return next_head;
    }
    pair<ListNode*, ListNode*> merge(ListNode* &h1, ListNode* &h2)
    {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        while (h1 && h2)
        {
            if (h1->val > h2->val)
            {
                cur->next = h2;
                h2 = h2->next;
            }
            else
            {
                cur->next = h1;
                h1 = h1->next;
            }
            cur = cur->next;
        }
        cur->next = h1 ? h1 : h2;
        while (cur->next)
        {
            cur = cur->next;
        }
        return {dummy->next, cur};
    }
};
// @lc code=end

class Solution {
    public:
        ListNode* sortList(ListNode* head) {
            if (! head || ! head->next) return head;
            ListNode* head2 = split(head);
            head = sortList(head);
            head2 = sortList(head2);
            return merge(head, head2);
        }
    private:
        ListNode* split(ListNode* &n)
        {
            ListNode* slow = n;
            ListNode* fast = n;
            ListNode* pre = new ListNode(0);
            pre->next = slow;
            while (fast && fast->next)
            {
                pre = slow;
                fast = fast->next->next;
                slow = slow->next;
            }
            ListNode* tmp = pre->next;
            pre->next = NULL;
            return tmp;
        }
        ListNode* merge(ListNode* h1, ListNode* h2)
        {
            ListNode* dummy = new ListNode(0);
            ListNode* cur = dummy;
            while (h1 && h2)
            {
                if (h1->val > h2->val)
                {
                    cur->next = h2;
                    h2 = h2->next;
                }
                else
                {
                    cur->next = h1;
                    h1 = h1->next;
                }
                cur = cur->next;
            }
            cur->next = h1 ? h1 : h2;
            return dummy->next;
        }
    };


class Solution {
    public:
        ListNode* sortList(ListNode* head) {
            vector<int> backup;
            ListNode* dummy = new ListNode(0);
            dummy->next = head;
            while (head)
            {
                backup.push_back(head->val);
                head = head->next;
            }
            ListNode* p = dummy->next;
            ranges::sort(backup);
            for (auto x : backup)
            {
                p->val = x;
                p = p->next;
            }
            return dummy->next;
        }
    };