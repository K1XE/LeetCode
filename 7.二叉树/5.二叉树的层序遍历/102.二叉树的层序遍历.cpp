/*
 * @lc app=leetcode.cn id=102 lang=cpp
 *
 * [102] 二叉树的层序遍历
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> q;
        if (root) q.push(root);
        while (q.size())
        {
            int n = q.size();
            vector<int> level;
            for (int i = 0; i < n; i ++ )
            {
                TreeNode* tmp = q.front();
                q.pop();
                level.push_back(tmp->val);
                if (tmp->left) q.push(tmp->left);
                if (tmp->right) q.push(tmp->right);
            }
            res.push_back(level);
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        vector<vector<int>> levelOrder(TreeNode* root) {
            vector<vector<int>> res;
            vector<int> level;
            TreeNode* q[2005];
            int front = 0, rear = 0, end = 0;
            if (root) q[rear ++] = root, end = 1;
            while (front < rear)
            {
                TreeNode* tmp = q[front ++];
                level.push_back(tmp->val);
                if (tmp->left) q[rear ++] = tmp->left;
                if (tmp->right) q[rear ++] = tmp->right;
                if (front == end)
                {
                    res.push_back(level);
                    end = rear;
                    level.clear();
                }
            }
            return res;
        }
    };
