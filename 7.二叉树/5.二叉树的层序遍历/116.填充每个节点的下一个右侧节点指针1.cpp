/*
 * @lc app=leetcode.cn id=116 lang=cpp
 *
 * [116] 填充每个节点的下一个右侧节点指针
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node {
    public:
        int val;
        Node* left;
        Node* right;
        Node* next;
        Node (int _val, Node* _left, Node* _right, Node* _next)
        {
            val = _val;
            left = _left;
            right = _right;
            next = _next;
        }
};
// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (! root) return nullptr;
        Node* p = root;
        while (p->left)
        {
            Node* no1 = p;
            while (no1)
            {
                no1->left->next = no1->right;
                if (no1->next)
                {
                    no1->right->next = no1->next->left;
                }
                no1 = no1->next;
            }
            p = p->left;
        }
        return root;
    }

};
// @lc code=end

class Solution {
    public:
        Node* connect(Node* root) {
            dfs(root);
            return root;
        }
    private:
        void dfs(Node* n)
        {
            if (! n) return;
            if (n->left && n->right)
            {
                n->left->next = n->right;
                if (n->next && n->right) n->right->next = n->next->left;
            }
            dfs(n->left);
            dfs(n->right);
        }
    };