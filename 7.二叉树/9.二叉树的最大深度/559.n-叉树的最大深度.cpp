/*
 * @lc app=leetcode.cn id=559 lang=cpp
 *
 * [559] N 叉树的最大深度
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node {
    public:
        int val;
        vector<Node*> children;
        Node(int _val, vector<Node*> _children)
        {
            val = _val;
            children = _children;
        }
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
    int maxDepth(Node* root) {
        queue<Node*> q;
        if (root) q.push(root);
        int depth = 0;
        while (q.size())
        {
            int n = q.size();
            while (n --)
            {
                Node* tmp = q.front();
                q.pop();
                for (auto p : tmp->children)
                {
                    q.push(p);
                }
            }
            depth ++;
        }
        return depth;
    }
};
// @lc code=end
class Solution {
    public:
        int maxDepth(Node* root) {
            if (! root) return 0;
            int maxD = 0;
            for (auto p : root->children)
            {
                maxD = max(maxD, maxDepth(p));
            }
            return maxD + 1;
        }
    };
