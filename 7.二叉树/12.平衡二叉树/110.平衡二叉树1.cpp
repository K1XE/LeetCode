/*
 * @lc app=leetcode.cn id=110 lang=cpp
 *
 * [110] 平衡二叉树
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        unordered_map<TreeNode*, int> h;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [node, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                if (abs(h[node->left] - h[node->right]) > 1) return 0;
                h[node] = max(h[node->left], h[node->right]) + 1;
                continue;
            }
            stk.emplace(node, 1);
            if (node->right) stk.emplace(node->right, 0);
            if (node->left) stk.emplace(node->left, 0);
        }
        return 1;
    }
};
// @lc code=end

class Solution {
    public:
        bool isBalanced(TreeNode* root) {
            return dfs(root) == -1 ? 0 : 1;
        }
    private:
        int dfs(TreeNode* n)
        {
            if (! n) return 0;
            int l = dfs(n->left);
            int r = dfs(n->right);
            if (l == -1 || r == -1) return -1;
            if (abs(l - r) > 1) return -1;
            return max(l, r) + 1;
        }
    };