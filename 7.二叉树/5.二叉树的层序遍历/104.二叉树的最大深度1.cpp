/*
 * @lc app=leetcode.cn id=104 lang=cpp
 *
 * [104] 二叉树的最大深度
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
    int maxDepth(TreeNode* root) {
        TreeNode* q[10005];
        int front = 0, rear = 0, end = 0, level = 0;
        if (root) q[rear ++] = root, end ++;
        while (front < rear)
        {
            TreeNode* tmp = q[front ++];
            if (tmp->left) q[rear ++] = tmp->left;
            if (tmp->right) q[rear ++] = tmp->right;
            if (front == end)
            {
                end = rear;
                level ++;
            }
        }
        return level;
    }
};
// @lc code=end

class Solution {
    public:
        int maxDepth(TreeNode* root) {
            return getDepth(root);
        }
    private:
        int getDepth(TreeNode* n)
        {
            if (! n) return 0;
            int l = getDepth(n->left);
            int r = getDepth(n->right);
            return max(l, r) + 1;
        }
    };