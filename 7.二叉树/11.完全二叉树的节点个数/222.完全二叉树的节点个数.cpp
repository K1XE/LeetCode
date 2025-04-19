/*
 * @lc app=leetcode.cn id=222 lang=cpp
 *
 * [222] 完全二叉树的节点个数
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
    int countNodes(TreeNode* root) {
        if (! root) return 0;
        TreeNode* tl = root->left;
        TreeNode* tr = root->right;
        int lh = 0, rh = 0;
        while (tl) tl = tl->left, lh ++;
        while (tr) tr = tr->right, rh ++;
        if (lh == rh) return (2 << lh) - 1;
        return countNodes(root->left) + countNodes(root->right) + 1;
    }
};
// @lc code=end

class Solution {
    public:
        int countNodes(TreeNode* root) {
            queue<TreeNode*> q;
            int cnt = 0;
            if (root) q.push(root);
            while (q.size())
            {
                int n = q.size();
                cnt += n;
                while (n --)
                {
                    TreeNode* tmp = q.front();
                    q.pop();
                    if (tmp->left) q.push(tmp->left);
                    if (tmp->right) q.push(tmp->right);
                }
            }
            return cnt;
        }
    };