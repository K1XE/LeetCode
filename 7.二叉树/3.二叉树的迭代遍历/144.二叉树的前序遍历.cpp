/*
 * @lc app=leetcode.cn id=144 lang=cpp
 *
 * [144] 二叉树的前序遍历
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
    vector<int> preorderTraversal(TreeNode* root) {
        TreeNode* p = root;
        vector<int> res;
        stack<TreeNode*> stk;
        while (stk.size() || p)
        {
            while (p)
            {
                res.push_back(p->val);
                stk.push(p);
                p = p->left;
            }
            p = stk.top()->right;
            stk.pop();
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> preorderTraversal(TreeNode* root) {
            vector<int> res;
            preOrder(root, res);
            return res;
        }
    private:
        void preOrder(TreeNode* n, vector<int>& res)
        {
            if (n == nullptr) return;
            res.push_back(n->val);
            preOrder(n->left, res);
            preOrder(n->right, res);
        }
    };
