/*
 * @lc app=leetcode.cn id=501 lang=cpp
 *
 * [501] 二叉搜索树中的众数
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
    vector<int> res;
    TreeNode* pre = nullptr;
    int cnt = 0, maxCnt = 0;
    vector<int> findMode(TreeNode* root) {
        dfs(root);
        return res;
    }
private:
    void dfs(TreeNode* n)
    {
        if (! n) return;
        dfs(n->left);
        if (pre && pre->val == n->val)
        {
            cnt ++;
        }
        else
        {
            cnt = 1;
        }
        if (cnt > maxCnt)
        {
            maxCnt = cnt;
            res.clear();
            res.emplace_back(n->val);
        }
        else if (cnt == maxCnt)
        {
            res.emplace_back(n->val);
        }
        pre = n;
        dfs(n->right);
    }
};
// @lc code=end

