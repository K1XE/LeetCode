/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
 */
#include <bits/stdc++.h>
using namespace std;
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
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 class Solution {
    public:
        ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
            ListNode* dummy = new ListNode(0);
            dummy->next = headA;
            ListNode* p = headA;
            int cntA = 0, cntB = 0;
            while (p)
            {
                cntA ++;
                p = p->next;
            }
            p = headB;
            while (p)
            {
                cntB ++;
                p = p->next;
            }
            ListNode* pa = headA;
            ListNode* pb = headB;
            if (cntA > cntB)
            {
                int diff = cntA - cntB;
                while (diff --)
                {
                    pa = pa->next;
                }
            }
            else
            {
                int diff = cntB - cntA;
                while (diff --)
                {
                    pb = pb->next;
                }
            }
            while (pa && pb)
            {
                if (pa == pb) return pa;
                pa = pa->next;
                pb = pb->next;
            }
            return nullptr;
        }
    };
    
// @lc code=end

