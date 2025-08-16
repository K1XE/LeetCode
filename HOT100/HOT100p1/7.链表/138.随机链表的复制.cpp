/*
 * @lc app=leetcode.cn id=138 lang=cpp
 *
 * [138] 随机链表的复制
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node
{
    public:
        int val;
        Node* next;
        Node* random;
        Node(int x, Node* p, Node* q)
        {
            val = x;
            next = p;
            random = q;
        }
};
// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (! head) return NULL;
        for (Node* cur = head; cur; cur = cur->next->next)
        {
            cur->next = new Node(cur->val, cur->next, NULL);
        }
        for (Node* cur = head; cur; cur = cur->next->next)
        {
            if (cur->random)
            {
                cur->next->random = cur->random->next;
            }
        }
        Node* new_head = head->next;
        Node* cur = head;
        Node* copy = cur->next;

        for (; cur->next->next; cur = cur->next)
        {
            cur->next = copy->next;
            copy->next = cur->next->next;
            copy = copy->next;
        }
        cur->next = NULL;
        return new_head;
    }
};
// @lc code=end
// class Node
// {
//     public:
//         int val;
//         Node* next;
//         Node* random;
//         Node(int x)
//         {
//             val = x;
//             next = NULL;
//             random = NULL;
//         }
// };
// class Solution {
//     public:
//         Node* copyRandomList(Node* head) {
//             if (! head) return NULL;
//             Node* dummy = new Node(0);
//             Node* p = new Node(0);
//             dummy->next = p;
//             Node* cur = head;
//             while (cur)
//             {
//                 p->val = cur->val;
//                 cur = cur->next;
//                 if (cur)
//                 {
//                     Node* post = new Node(0);
//                     p->next = post;
//                     p = post;
//                 }
//             }
//             p = dummy->next;
//             cur = head;
//             while (cur)
//             {
//                 Node* rdm = head;
//                 int cnt = 0;
//                 while (rdm && rdm != cur->random)
//                 {
//                     cnt ++;
//                     rdm = rdm->next;
//                 }
//                 Node* tmp = dummy->next;
//                 while (tmp && cnt) tmp = tmp->next, cnt --;
//                 p->random = cur->random ? tmp : NULL;
//                 p = p->next;
//                 cur = cur->next;
//             }
//             return dummy->next;
//         }
//     };
    