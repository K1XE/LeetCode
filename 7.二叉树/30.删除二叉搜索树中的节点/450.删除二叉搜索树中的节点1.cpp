/*
 * @lc app=leetcode.cn id=450 lang=cpp
 *
 * [450] 删除二叉搜索树中的节点
 */
#include <bits/stdc++.h>
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
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* pre = NULL;
        TreeNode* cur = root;
        while (cur)
        {
            if (cur->val == key) break;
            pre = cur;
            if (cur->val > key) cur = cur->left;
            else cur = cur->right;
        }
        if (! pre) return delete_this_node(cur);
        if (pre->left && pre->left->val == key) pre->left = delete_this_node(pre->left);
        if (pre->right && pre->right->val == key) pre->right = delete_this_node(pre->right);
        return root;
    }
    TreeNode* delete_this_node(TreeNode* n)
    {
        if (! n) return NULL;
        else if (! n->right) return n->left;
        else
        {
            TreeNode* cur = n->right;
            while (cur->left)
            {
                cur = cur->left;
            }
            cur->left = n->left;
            return n->right;
        }
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* deleteNode(TreeNode* root, int key) {
            if (! root) return NULL;
            if (root->val == key)
            {
                if (! root->left && ! root->right)
                {
                    delete root;
                    return NULL;
                }
                else if (! root->right)
                {
                    TreeNode* tmp = root->left;
                    delete root;
                    return tmp;
                }
                else
                {
                    TreeNode* cur = root->right;
                    while (cur->left)
                    {
                        cur = cur->left;
                    }
                    cur->left = root->left;
                    TreeNode* tmp = root->right;
                    delete root;
                    return tmp;
                }
            }
            root->left = deleteNode(root->left, key);
            root->right = deleteNode(root->right, key);
            return root;
        }
    };