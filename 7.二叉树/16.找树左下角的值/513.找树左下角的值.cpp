/*
 * @lc app=leetcode.cn id=513 lang=cpp
 *
 * [513] 找树左下角的值
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
    int max_d = INT_MIN;
    int res = -1;
    int findBottomLeftValue(TreeNode* root) {
        dfs(root, 1);
        return res;
    }
private:
    void dfs(TreeNode* n, int depth)
    {
        if (! n) return;
        if (! n->left && ! n->right)
        {
            if (max_d < depth)
            {
                max_d = depth;
                res = n->val;
            }
        }
        if (n->left)
        {
            depth ++;
            dfs(n->left, depth);
            depth --;
        }
        if (n->right)
        {
            depth ++;
            dfs(n->right, depth);
            depth --;
        }
    }
};
// @lc code=end

class Solution {
    public:
        int findBottomLeftValue(TreeNode* root) {
            queue<TreeNode*> q;
            if (root) q.emplace(root);
            int res = -1;
            while (q.size())
            {
                int n = q.size();
                res = q.front()->val;
                while (n -- )
                {
                    TreeNode* tmp = q.front();
                    q.pop();
                    if (tmp->left) q.emplace(tmp->left);
                    if (tmp->right) q.emplace(tmp->right);
                }
            }
            return res;
        }
    };