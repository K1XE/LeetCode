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
    int max_d = INT_MIN;
    int maxDepth(Node* root) {
        dfs(root, 0);
        return root ? max_d + 1 : 0;
    }
private:
    void dfs(Node* n, int d)
    {
        if (! n) return;
        max_d = max(max_d, d);
        for (auto p : n->children)
        {
            dfs(p, d + 1);
        }
    }
};
// @lc code=end

