/*
 * @lc app=leetcode.cn id=1038 lang=cpp
 *
 * [1038] 从二叉搜索树到更大和树
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct TreeNode
{
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
    int pre = 0;
    TreeNode* bstToGst(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [node, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                node->val += pre;
                pre = node->val;
                continue;
            }
            if (node->left) stk.emplace(node->left, 0);
            stk.emplace(node, 1);
            if (node->right) stk.emplace(node->right, 0);
        }
        return root;
    }
};
// @lc code=end

