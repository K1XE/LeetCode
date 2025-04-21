/*
 * @lc app=leetcode.cn id=107 lang=cpp
 *
 * [107] 二叉树的层序遍历 II
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> res;
        int level = 0;
        if (root) q.emplace(root);
        while (q.size())
        {
            int n = q.size();
            while (n --)
            {
                TreeNode* tmp = q.front();
                q.pop();
                if (level == res.size()) res.emplace_back();
                res[level].emplace_back(tmp->val);
                if (tmp->left) q.emplace(tmp->left);
                if (tmp->right) q.emplace(tmp->right);
            }
            level ++;
        }
        ranges::reverse(res);
        return res;
    }
};
// @lc code=end

