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
        stack<TreeNode*> stk;
        if (root) stk.emplace(root);
        while (stk.size())
        {
            TreeNode* cur = stk.top();
            if (cur->val > p->val && cur->val > q->val)
            {
                if (cur->left)
                {
                    stk.push(cur->left);
                    continue;
                }
            }
            if (cur->val < p->val && cur->val < q->val)
            {
                if (cur->right)
                {
                    stk.push(cur->right);
                    continue;
                }
            }
            return cur;
        }
        return nullptr;
    }
};
// @lc code=end


class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            return dfs(root, p, q);
        }
    private:
        TreeNode* dfs(TreeNode* cur, TreeNode* p, TreeNode* q)
        {
            if (! cur) return nullptr;
            if (cur->val > p->val && cur->val > q->val) 
            {
                TreeNode* l = dfs(cur->left, p, q);
                if (l) return l;
            }
            if (cur->val < p->val && cur->val < q->val)
            {
                TreeNode* r = dfs(cur->right, p, q);
                if (r) return r;
            }
            return cur;
        }
    };

class Solution {
    public:
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            return dfs(root, p, q);
        }
    private:
        TreeNode* dfs(TreeNode* root, TreeNode* p, TreeNode* q)
        {
            if (! root || root == p || root == q) return root;
            TreeNode* l = dfs(root->left, p, q);
            TreeNode* r = dfs(root->right, p, q);
            if (l && r) return root;
            else if (! l && r) return r;
            else if (l && ! r) return l;
            else return nullptr;
        }
    };