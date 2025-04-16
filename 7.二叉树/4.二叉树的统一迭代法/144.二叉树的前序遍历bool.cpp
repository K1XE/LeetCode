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
        stack<pair<TreeNode*, bool>> stk;
        vector<int> res;
        if (! root) return res;
        stk.push({root, 0});
        while (stk.size())
        {
            auto tmp = stk.top();
            stk.pop();
            if (tmp.second == 1)
            {
                res.push_back(tmp.first->val);
                continue;
            }
            if (tmp.first->right) stk.push({tmp.first->right, 0});
            if (tmp.first->left) stk.push({tmp.first->left, 0});
            stk.push({tmp.first, 1});
        }
        return res;
    }
};
// @lc code=end
