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
        queue<TreeNode*> q;
        vector<int> res;
        if (root) q.emplace(root);
        while (q.size())
        {
            int n = q.size();
            int maxVal = INT_MIN;
            while (n --)
            {
                TreeNode* tmp = q.front();
                maxVal = max(maxVal, tmp->val);
                q.pop();
                if (tmp->left) q.emplace(tmp->left);
                if (tmp->right) q.emplace(tmp->right);
                if (! n) res.push_back(maxVal);
            }
        }
        return res;
    }
};
// @lc code=end

