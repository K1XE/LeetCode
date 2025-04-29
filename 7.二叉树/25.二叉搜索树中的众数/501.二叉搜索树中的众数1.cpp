/*
 * @lc app=leetcode.cn id=501 lang=cpp
 *
 * [501] 二叉搜索树中的众数
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
    int cnt = 1, maxCnt = 1;
    long long pre = LLONG_MAX;
    vector<int> res;
    vector<int> findMode(TreeNode* root) {
        stack<pair<TreeNode*, bool>> stk;
        if (root) stk.emplace(root, 0);
        while (stk.size())
        {
            auto [node, visit] = stk.top();
            stk.pop();
            if (visit)
            {
                if (pre != LLONG_MAX && pre == node->val) cnt ++;
                else cnt = 1;
                pre = node->val;
                if (cnt > maxCnt)
                {
                    maxCnt = cnt;
                    res.clear();
                    res.emplace_back(node->val);
                }
                else if (cnt == maxCnt)
                {
                    res.emplace_back(node->val);
                }
                continue;
            }
            if (node->right) stk.emplace(node->right, 0);
            stk.emplace(node, 1);
            if (node->left) stk.emplace(node->left, 0);
        }
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        int cnt = 1, maxCnt = 1;
        long long pre = LLONG_MAX;
        vector<int> res;
        vector<int> findMode(TreeNode* root) {
            dfs(root);
            return res;
        }
    private:
        void dfs(TreeNode* n)
        {
            if (! n) return;
            dfs(n->left);
            if (pre != LLONG_MAX && n->val == pre) cnt ++; 
            else cnt = 1;
            pre = n->val;
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
            dfs(n->right);
        }
    };