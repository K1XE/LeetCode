/*
 * @lc app=leetcode.cn id=114 lang=cpp
 *
 * [114] 二叉树展开为链表
 */
#include "tools.h"
struct TreeNode
{
    int val;
    TreeNode *left, *right;
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
class Solution
{
public:
    void flatten(TreeNode *root)
    {
        TreeNode *n = root;
        while (n)
        {
            if (n->left)
            {
                TreeNode *tmpr = n->right;
                TreeNode *cur = n->left;
                TreeNode *tmpl = cur;
                while (cur->right) cur = cur->right;
                n->left = NULL;
                n->right = tmpl;
                cur->right = tmpr;
            }
            n = n->right;
        }
    }
};
// @lc code=end

class Solution
{
public:
    void flatten(TreeNode *root)
    {

        auto dfs = [&](auto &&self, TreeNode *n)
        {
            if (!n)
                return;
            if (n->left)
            {
                TreeNode *tmpr = n->right;
                TreeNode *cur = n->left;
                n->right = cur;
                while (cur->right)
                    cur = cur->right;
                cur->right = tmpr;
                n->left = NULL;
            }
            self(self, n->right);
        };
        dfs(dfs, root);
    }
};