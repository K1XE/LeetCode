/*
 * @lc app=leetcode.cn id=590 lang=cpp
 *
 * [590] N 叉树的后序遍历
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node {
    public:
        int val;
        vector<Node*> children;
        Node(int _val, vector<Node*> _children) : val(_val), children(_children) {}
};
// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> res;
    vector<int> postorder(Node* root) {
        stack<pair<Node*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [node, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                res.push_back(node->val);
                continue;
            }
            stk.emplace(node, 1);
            for (int i = node->children.size() - 1; i >= 0; i -- )
            {
                stk.emplace(node->children[i], 0);
            }
        }
        return res;
    }
};
// @lc code=end

// sol1
class Solution {
    public:
        vector<int> res;
        vector<int> postorder(Node* root) {
            stack<Node*> stk;
            Node* p = root;
            Node* pre;
            while (stk.size() || p)
            {
                if (p)
                {
                    stk.push(p);
                    p = p->children.empty() ? nullptr : p->children[0];
                }
                else
                {
                    Node* tmp = stk.top();
    
                    if (tmp->children.size() && pre != tmp->children.back())
                    {
                        int i = 0;
                        while (i < tmp->children.size() - 1 && pre != tmp->children[i])
                        {
                            i ++;
                        }
                        p = tmp->children[i + 1];
                    }
                    else
                    {
                        stk.pop();
                        res.push_back(tmp->val);
                        pre = tmp;
                    }
                }
            }
            return res;
        }
    };

// sol2
class Solution {
    public:
        vector<int> res;
        vector<int> postorder(Node* root) {
            dfs(root);
            return res;
        }
    private:
        void dfs(Node* n)
        {
            if (! n) return;
            for (auto p : n->children)
            {
                dfs(p);
            }
            res.push_back(n->val);
        }
    
    };