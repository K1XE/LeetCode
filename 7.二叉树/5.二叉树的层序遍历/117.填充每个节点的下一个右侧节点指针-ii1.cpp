/*
 * @lc app=leetcode.cn id=117 lang=cpp
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
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
        Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}
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
            while (p)
            {
                Node dummy(0);
                Node* tail = &dummy;
                while (p)
                {
                    if (p->left)
                    {
                        tail->next = p->left;
                        tail = tail->next;
                    }
                    if (p->right)
                    {
                        tail->next = p->right;
                        tail = tail->next;
                    }
                    p = p->next;
                }
                p = dummy.next;
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
            Node* nextChild = getNext(n->next);
            if (n->left)
            {
                if (n->right) n->left->next = n->right;
                else n->left->next = nextChild;
            }
            if (n->right)
            {
                n->right->next = nextChild;
            }
            dfs(n->right);
            dfs(n->left);
        }
        Node* getNext(Node* n)
        {
            while (n)
            {
                if (n->left) return n->left;
                if (n->right) return n->right;
                n = n->next;
            }
            return nullptr;
        }
    };