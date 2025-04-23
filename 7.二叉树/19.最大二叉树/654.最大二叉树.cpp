/*
 * @lc app=leetcode.cn id=654 lang=cpp
 *
 * [654] 最大二叉树
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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if (! nums.size()) return nullptr;
        return dfs(nums, 0, nums.size() - 1);
    }
private:
    TreeNode* dfs(vector<int>& nums, int l, int r)
    {
        if (l > r) return nullptr;
        int maxVal = INT_MIN, mid = -1;
        for (int i = l; i <= r; i ++ )
        {
            if (nums[i] > maxVal) maxVal = nums[i], mid = i;
        }
        TreeNode* root = new TreeNode(maxVal);
        if (l == r) return root;
        int ll = l, lr = mid - 1;
        int rl = mid + 1, rr = r;
        root->left = dfs(nums, ll, lr);
        root->right = dfs(nums, rl, rr);
        return root;
    }
};
// @lc code=end

