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
        Node(int _val, Node* _left, Node* _right, Node* _next) :
            val(_val), left(_left), right(_right), next(_next) {}
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
        queue<Node*> q;
        if (! root) return nullptr;
        q.push(root);
        while (q.size())
        {
            int n = q.size();
            for (int i = 0; i < n; i ++ )
            {
                Node* tmp = q.front();
                q.pop();
                if (tmp->left) q.push(tmp->left);
                if (tmp->right) q.push(tmp->right);
                if (i < n - 1)
                {
                    Node* nxt = q.front();
                    tmp->next = nxt;
                }
            }
        }
        return root;
    }
};
// @lc code=end

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