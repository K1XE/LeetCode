/*
 * @lc app=leetcode.cn id=515 lang=cpp
 *
 * [515] 在每个树行中找最大值
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
    vector<int> largestValues(TreeNode* root) {
        vector<int> res;
        queue<TreeNode*> q;
        if (root) q.push(root);
        while (q.size())
        {
            int maxVal = INT32_MIN;
            int n = q.size();
            while (n --)
            {
                TreeNode* tmp = q.front();
                q.pop();
                if (tmp->left) q.push(tmp->left);
                if (tmp->right) q.push(tmp->right);
                maxVal = max(maxVal, tmp->val);
            }
            res.push_back(maxVal);
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        vector<int> largestValues(TreeNode* root) {
            vector<int> res;
            TreeNode* q[10005];
            int front = 0, rear = 0, end = 0, maxVal = INT32_MIN;
            if (root) q[rear ++] = root, end ++;
            while (front < rear)
            {
                TreeNode* tmp = q[front ++];
                maxVal = max(maxVal, tmp->val);
                if (tmp->left) q[rear ++] = tmp->left;
                if (tmp->right) q[rear ++] = tmp->right;
                if (front == end)
                {
                    end = rear;
                    res.push_back(maxVal);
                    maxVal = INT32_MIN;
                }
            }
            return res;
        }
    };
