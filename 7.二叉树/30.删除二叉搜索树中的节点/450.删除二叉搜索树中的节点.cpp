/*
 * @lc app=leetcode.cn id=450 lang=cpp
 *
 * [450] 删除二叉搜索树中的节点
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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (! root) return root;
        if (root->val == key)
        {
            if (! root->right) return root->left;
            TreeNode* cur = root->right;
            while (cur->left)
            {
                cur = cur->left;
            }
            swap(cur->val, root->val);
        }
        root->left = deleteNode(root->left, key);
        root->right = deleteNode(root->right, key);
        return root;
    }
};
// @lc code=end


class Solution {
    public:
        TreeNode* deleteNode(TreeNode* root, int key) {
            if (! root) return root;
            TreeNode* cur = root;
            TreeNode* pre = nullptr;
            while (cur)
            {
                if (cur->val == key) break;
                pre = cur;
                if (cur->val > key) cur = cur->left;
                else cur = cur->right;
            }
            if (! pre) return delete_this_node(root);
            if (pre->left && pre->left->val == key) pre->left = delete_this_node(pre->left);
            if (pre->right && pre->right->val == key) pre->right = delete_this_node(pre->right);
            return root;
        }
    private:
        TreeNode* delete_this_node(TreeNode* n)
        {
            if (! n) return nullptr;
            if (! n->right) return n->left;
            TreeNode* cur = n->right;
            while (cur->left) cur = cur->left;
            cur->left = n->left;
            return n->right;
        }
    };

class Solution {
    public:
        TreeNode* deleteNode(TreeNode* root, int key) {
            if (! root) return NULL;
            if (root->val == key)
            {
                if (! root->left && ! root->right)
                {
                    delete root;
                    return nullptr;
                }
                else if (! root->left)
                {
                    TreeNode* tmp = root->right;
                    delete root;
                    return tmp;
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
            if (root->val > key) root->left = deleteNode(root->left, key);
            if (root->val < key) root->right = deleteNode(root->right, key);
            return root;
        }
    };