/*
 * @lc app=leetcode.cn id=429 lang=cpp
 *
 * [429] N 叉树的层序遍历
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Node {
    public:
        int val;
        vector<Node*> children;
        Node(int _val, vector<Node*> _c) : val(_val), children(_c) {}
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
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> res;
        int front = 0, rear = 0, end = 0, level = 0;
        Node* q[10005];
        if (root) q[rear ++] = root, end ++;
        while (front < rear)
        {
            Node* tmp = q[front ++];
            if (res.size() == level) res.emplace_back();
            res[level].emplace_back(tmp->val);
            for (auto p : tmp->children)
            {
                q[rear ++] = p;
            }
            if (front == end)
            {
                level ++;
                end = rear;
            }
        }
        return res;
    }
};
// @lc code=end

