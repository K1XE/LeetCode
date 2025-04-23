/*
 * @lc app=leetcode.cn id=113 lang=cpp
 *
 * [113] 路径总和 II
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
    vector<vector<int>> res;
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        int top = -1, cnt = 0;
        TreeNode* stk[5010];
        TreeNode* cur = root;
        TreeNode* pre;
        while (top >= 0 || cur)
        {
            if (cur)
            {
                stk[++ top] = cur;
                cur = cur->left;
            }
            else
            {
                TreeNode* tmp = stk[top];
                if (tmp->right && tmp->right != pre)
                {
                    cur = tmp->right;
                }
                else
                {
                    if (! tmp->left && ! tmp->right)
                    {
                        int sums = 0;
                        for (int i = 0; i <= top; i ++ )
                        {
                            sums += stk[i]->val;
                        }
                        if (sums == targetSum)
                        {
                            if (res.size() == cnt) res.emplace_back();
                            for (int i = 0; i <= top; i ++ )
                            {
                                res[cnt].push_back(stk[i]->val);
                            }
                            cnt ++;
                        }
                    }
                    -- top;
                    pre = tmp;
                }
            }
        }
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        vector<int> path;
        vector<vector<int>> res;
        vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
            if (! root) return {};
            path.push_back(root->val);
            dfs(root, path, targetSum);
            return res;
        }
    private:
        void dfs(TreeNode* n, vector<int>& path, int t)
        {
            if (! n->left && ! n->right)
            {
                int sums = 0;
                for (auto x : path) sums += x;
                if (sums == t)
                {
                    res.emplace_back(path);
                }
                return;
            }
            if (n->left)
            {
                path.push_back(n->left->val);
                dfs(n->left, path, t);
                path.pop_back();
            }
            if (n->right)
            {
                path.push_back(n->right->val);
                dfs(n->right, path, t);
                path.pop_back();
            }
        }
    };