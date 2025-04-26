/*
 * @lc app=leetcode.cn id=108 lang=cpp
 *
 * [108] 将有序数组转换为二叉搜索树
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
struct TreeNode
{
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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode* node = dfs(nums, 0, nums.size() - 1);
        return node;
    }
private:
    TreeNode* dfs(vector<int>& nums, int l, int r)
    {
        if (l > r) return NULL;
        int mid = l + r >> 1;
        TreeNode* cur = new TreeNode(nums[mid]);
        cur->left = dfs(nums, l, mid - 1);
        cur->right = dfs(nums, mid + 1, r);
        return cur;
    }
};
// @lc code=end

