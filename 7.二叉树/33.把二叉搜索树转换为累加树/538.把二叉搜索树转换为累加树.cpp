/*
 * @lc app=leetcode.cn id=538 lang=cpp
 *
 * [538] 把二叉搜索树转换为累加树
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
    int pre = 0;
    TreeNode* convertBST(TreeNode* root) {
        dfs(root);
        return root;
    }
private:
    void dfs(TreeNode* n)
    {
        if (! n) return;
        dfs(n->right);
        n->val += pre;
        pre = n->val;
        dfs(n->left);
    }
};
// @lc code=end

class Solution {
    public:
        vector<int> nums;
        int cnt = 0;
        int sums = 0;
        TreeNode* convertBST(TreeNode* root) {
            dfs1(root);
            for (int i = 0; i < nums.size(); i ++ )
            {
                int tmp = nums[i];
                nums[i] = sums;
                sums -= tmp;
            }
            dfs2(root);
            return root;
        }
    private:
        void dfs1(TreeNode* n)
        {
            if (! n) return;
            dfs1(n->left);
            nums.push_back(n->val);
            sums += n->val;
            dfs1(n->right);
        }
        void dfs2(TreeNode* n)
        {
            if (! n) return;
            dfs2(n->left);
            n->val = nums[cnt ++];
            dfs2(n->right);
        }
    };