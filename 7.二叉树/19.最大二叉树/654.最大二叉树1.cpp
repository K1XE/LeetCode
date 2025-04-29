/*
 * @lc app=leetcode.cn id=654 lang=cpp
 *
 * [654] 最大二叉树
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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return dfs(nums, 0, nums.size() - 1);
    }
    TreeNode* dfs(vector<int>& nums, int l, int r)
    {
        if (l > r) return NULL;
        int maxval = -1, maxidx = -1;
        for (int i = l; i <= r; i ++ )
        {
            if (nums[i] > maxval)
            {
                maxval = nums[i];
                maxidx = i;
            }
        }
        int tmp = nums[maxidx];
        TreeNode* p = new TreeNode(tmp);
        int ll = l, lr = maxidx - 1, rl = maxidx + 1, rr = r;
        p->left = dfs(nums, ll, lr);
        p->right = dfs(nums, rl, rr);
        return p;
    }
};
// @lc code=end

