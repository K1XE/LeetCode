/*
 * @lc app=leetcode.cn id=199 lang=cpp
 *
 * [199] 二叉树的右视图
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        TreeNode* q[105];
        int front = 0, rear = 0, end = 0;
        if (root) q[rear ++] = root, end ++;
        while (front < rear)
        {
            TreeNode* tmp = q[front ++];
            if (tmp->left) q[rear ++] = tmp->left;
            if (tmp->right) q[rear ++] = tmp->right;
            if (front == end)
            {
                res.push_back(tmp->val);
                end = rear;
            }
        }
        return res;
    }
};
// @lc code=end

