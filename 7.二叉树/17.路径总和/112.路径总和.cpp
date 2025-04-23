/*
 * @lc app=leetcode.cn id=112 lang=cpp
 *
 * [112] 路径总和
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (! root) return 0;
        return dfs(root, targetSum - root->val);
    }
private:
    bool dfs(TreeNode* n, int t)
    {
        if (! n->left && ! n->right && ! t) return 1;
        if (! n->left && ! n->right) return 0;
        if (n->left)
        {
            t -= n->left->val;
            if (dfs(n->left, t)) return 1; // 符合条件了 直接返回
            t += n->left->val;
        }
        if (n->right)
        {
            t -= n->right->val;
            if (dfs(n->right, t)) return 1;
            t += n->right->val;
        }
        return 0;
    }
};
// @lc code=end


//sol1 dfs
class Solution {
    public:
        int sums = 0;
        bool flag = 0;
        vector<int> path;
        bool hasPathSum(TreeNode* root, int targetSum) {
            if (! root) return 0;
            path.push_back(root->val);
            dfs(root, path, targetSum);
            return flag;
        }
    private:
        void dfs(TreeNode* n, vector<int>& path, int t)
        {
            if (! n->left && ! n->right)
            {
                for (auto x : path) sums += x;
                if (sums == t)
                {
                    flag = 1;
                }
                sums = 0;
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

//sol2 post
class Solution {
    public:
        bool hasPathSum(TreeNode* root, int targetSum) {
            int top = -1;
            TreeNode* stk[5010];
            TreeNode* p = root;
            TreeNode* pre;
            while (top >= 0 || p)
            {
                if (p)
                {
                    stk[++ top] = p;
                    p = p->left;
                }
                else
                {
                    TreeNode* tmp = stk[top];
                    if (tmp->right && tmp->right != pre)
                    {
                        p = tmp->right;
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
                            if (sums == targetSum) return 1;
                        }
                        -- top;
                        pre = tmp;
                    }
                }
            }
            return 0;
        }
    };

