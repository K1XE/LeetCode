/*
 * @lc app=leetcode.cn id=101 lang=cpp
 *
 * [101] 对称二叉树
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
    bool isSymmetric(TreeNode* root) {
        stack<TreeNode*> stk;
        if (! root) return 1;
        stk.push(root->left), stk.push(root->right);
        while (stk.size())
        {
            TreeNode* tl = stk.top(); stk.pop();
            TreeNode* tr = stk.top(); stk.pop();
            if (! tl && ! tr) continue;
            if ((! tr && tl) || (tr && ! tl) || (tr->val != tl->val)) return 0;
            stk.push(tl->left), stk.push(tr->right);
            stk.push(tl->right), stk.push(tr->left);
        }
        return 1;
    }
};
// @lc code=end

class Solution {
    public:
        bool isSymmetric(TreeNode* root) {
            if (! root) return 1;
            return dfs(root->left, root->right);
        }
    private:
        bool dfs(TreeNode* l, TreeNode* r)
        {
            if (! l && ! r) return 1;
            else if (! l && r) return 0;
            else if (l && ! r) return 0;
            else if (l->val != r->val) return 0;
            bool b1 = dfs(l->left, r->right);
            bool b2 = dfs(l->right, r->left);
            return b1 && b2;
        }
    };