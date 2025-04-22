/*
 * @lc app=leetcode.cn id=257 lang=cpp
 *
 * [257] 二叉树的所有路径
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
    vector<string> res;
    vector<int> path;
    vector<string> binaryTreePaths(TreeNode* root) {
        if (! root) return {};
        dfs(root);
        return res;
    }
private:
    void dfs(TreeNode* n)
    {
        path.emplace_back(n->val);
        if (! n->left && ! n->right)
        {
            string s;
            for (int i = 0; i < path.size(); i ++ )
            {
                s += to_string(path[i]);
                s += "->";
            }
            res.emplace_back(s.substr(0, s.size() - 2));
        }
        if (n->left)
        {
            dfs(n->left);
            path.pop_back();
        }
        if (n->right)
        {
            dfs(n->right);
            path.pop_back();
        }
    }
};
// @lc code=end

class Solution {
    public:
        vector<string> binaryTreePaths(TreeNode* root) {
            vector<string> res;
            TreeNode* stk[105];
            int top = -1;
            TreeNode* pre;
            TreeNode* cur = root;
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
                    if (tmp->right && pre != tmp->right)
                    {
                        cur = tmp->right;
                    }
                    else
                    {
                        string s;
                        if (! tmp->left && ! tmp->right)
                        {
                            for (int i = 0; i <= top; i ++ )
                            {
                                s += to_string(stk[i]->val);
                                s += "->";
                            }
                            res.emplace_back(s.substr(0, s.size() - 2));
                        }
                        top --;
                        pre = tmp;
                    }
                }
            }
            return res;
        }
    };