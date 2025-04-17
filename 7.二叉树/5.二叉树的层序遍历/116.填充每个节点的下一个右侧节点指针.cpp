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
        Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
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
        dfs(root, 0);
        return root;
    }
private:
    vector<Node*> pre;
    void dfs(Node* n, int depth)
    {
        if (! n) return;
        if (depth == pre.size()) pre.emplace_back(n);
        else 
        {
            pre[depth]->next = n;
            pre[depth] = n;
        }
        dfs(n->left, depth + 1);
        dfs(n->right, depth + 1);
    }
};
// @lc code=end

//sol 1
class Solution {
    public:
        Node* connect(Node* root) {
            if (!root) return nullptr;
            Node* left = root;
            while (left->left)
            {
                Node* head = left;
                while (head)
                {
                    head->left->next = head->right;
                    if (head->next)
                    {
                        head->right->next = head->next->left;
                    }
                    head = head->next;
                }
                left = left->left;
            }
            return root;
        }
    };

// sol2
class Solution {
    public:
        Node* connect(Node* root) {
            Node* q[4096];
            int front = 0, rear = 0, end = 0;
            if (root) q[rear ++] = root, end ++;
            while (front < rear)
            {
                Node* tmp = q[front ++];
                if (tmp->left) q[rear ++] = tmp->left;
                if (tmp->right) q[rear ++] = tmp->right;
                if (front < end)
                {
                    Node* nxt = q[front];
                    tmp->next = nxt;
                }
                if (front == end)
                {
                    end = rear;
                }
            }
            return root;
        }
    };