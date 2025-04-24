/*
 * @lc app=leetcode.cn id=617 lang=cpp
 *
 * [617] 合并二叉树
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
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        queue<TreeNode*> q;
        if (! root1 || ! root2) return root1 ? root1 : root2;
        q.emplace(root1), q.emplace(root2);
        while (q.size())
        {
            TreeNode* t1 = q.front(); q.pop();
            TreeNode* t2 = q.front(); q.pop();
            t1->val += t2->val;
            if (t1->right && t2->right)
            {
                q.emplace(t1->right), q.emplace(t2->right);
            }
            if (t1->left && t2->left)
            {
                q.emplace(t1->left), q.emplace(t2->left);
            }
            if (! t1->left && t2->left)
            {
                t1->left = t2->left;
            }
            if (! t1->right && t2->right)
            {
                t1->right = t2->right;
            }
        }
        return root1;
    }
};
// @lc code=end

class Solution {
    public:
        TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
            return dfs(root1, root2);
        }
    private:
        TreeNode* dfs(TreeNode* n1, TreeNode* n2)
        {
            if (! n1) return n2;
            if (! n2) return n1;
            n1->val += n2->val;
            n1->left = dfs(n1->left, n2->left);
            n1->right = dfs(n1->right, n2->right);
            return n1;
        }
    };