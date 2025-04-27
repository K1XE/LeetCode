/*
 * @lc app=leetcode.cn id=235 lang=cpp
 *
 * [235] 二叉搜索树的最近公共祖先
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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (! root) return nullptr;
        if (root->val > p->val && root->val > q->val)
        {
            TreeNode* l = lowestCommonAncestor(root->left, p, q);
            if (l) return l;
        }
        if (root->val < p->val && root->val < q->val)
        {
            TreeNode* r = lowestCommonAncestor(root->right, p, q);
            if (r) return r;
        }
        return root;
    }
};
// @lc code=end

