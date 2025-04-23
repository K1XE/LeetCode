/*
 * @lc app=leetcode.cn id=404 lang=cpp
 *
 * [404] 左叶子之和
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
    int sumOfLeftLeaves(TreeNode* root) {
        int front = 0, rear = 0, end = 0, sums = 0;
        TreeNode* q[1010];
        if (root) q[rear ++] = root, end ++;
        while (front < rear)
        {
            TreeNode* tmp = q[front ++];
            if (tmp->left) q[rear ++] = tmp->left;
            if (tmp->right) q[rear ++] = tmp->right;
            if (tmp->left && ! tmp->left->left && ! tmp->left->right)
            {
                sums += tmp->left->val;
            }
            if (front == end)
            {
                end = rear;
            }
        }
        return sums;
    }
};
// @lc code=end

// sol1 preOrder
class Solution {
    public:
        int sums = 0;
        int sumOfLeftLeaves(TreeNode* root) {
            dfs(root);
            return sums;
        }
    private:
        void dfs(TreeNode* n)
        {
            if (! n) return;
            if (n->left && ! n->left->left && ! n->left->right)
            {
                sums += n->left->val;
            }
            dfs(n->left);
            dfs(n->right);
        }
    };

// sol2 postOrder
class Solution {
    public:
        int sumOfLeftLeaves(TreeNode* root) {
            return dfs(root);
        }
    private:
        int dfs(TreeNode* n)
        {
            if (! n) return 0;
            int a = dfs(n->left);
            if (n->left && ! n->left->left && ! n->left->right)
            {
                a = n->left->val;
            }
            
            int b = dfs(n->right);
            return a + b;
        }
    };