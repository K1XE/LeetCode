/*
 * @lc app=leetcode.cn id=145 lang=cpp
 *
 * [145] 二叉树的后序遍历
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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.push({root, 0});
        while(stk.size())
        {
            auto t = stk.top();
            stk.pop();
            if (t.second)
            {
                res.push_back(t.first->val);
                continue;
            }
            stk.push({t.first, 1});
            if (t.first->right) stk.push({t.first->right, 0});
            if (t.first->left) stk.push({t.first->left, 0});
        }
        return res;
    }
};
// @lc code=end
