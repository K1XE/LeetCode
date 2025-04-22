/*
 * @lc app=leetcode.cn id=637 lang=cpp
 *
 * [637] 二叉树的层平均值
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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        int front = 0, rear = 0, end = 0;
        TreeNode* q[10005];
        if (root) q[rear ++] = root, end ++;
        double mean = 0;
        int cnt = 0;
        while (front < rear)
        {
            cnt ++;
            TreeNode* tmp = q[front ++];
            mean += tmp->val;
            if (tmp->left) q[rear ++] = tmp->left;
            if (tmp->right) q[rear ++] = tmp->right;
            if (front == end)
            {
                res.push_back(mean / cnt);
                cnt = 0, mean = 0;
                end = rear;
            }
        }
        return res;
    }
};
// @lc code=end

