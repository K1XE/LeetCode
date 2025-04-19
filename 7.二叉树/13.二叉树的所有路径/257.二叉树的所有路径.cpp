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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        stack<pair<TreeNode*, string>> stk;
        if (root) stk.push({root, to_string(root->val)});
        while (stk.size())
        {
            auto tmp = stk.top();
            stk.pop();
            if (! tmp.first->left && ! tmp.first->right)
            {
                res.push_back(tmp.second);
            }
            if (tmp.first->right)
            {
                stk.push({tmp.first->right, tmp.second + "->" + to_string(tmp.first->right->val)});
            }
            if (tmp.first->left)
            {
                stk.push({tmp.first->left, tmp.second + "->" + to_string(tmp.first->left->val)});
            }
        }
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        vector<string> binaryTreePaths(TreeNode* root) {
            if (! root) return {};
            vector<string> res;
            vector<int> path;
            dfs(root, path, res);
            return res;
        }
    private:
        void dfs(TreeNode* n, vector<int>& path, vector<string>& res)
        {
            path.push_back(n->val);
            if (! n->left && ! n->right)
            {
                string s;
                for (int i = 0; i < path.size(); i ++ )
                {
                    s += to_string(path[i]);
                    s += "->";
                }
                res.push_back(s.substr(0, s.size() - 2));
                return;
            }
            if (n->left)
            {
                dfs(n->left, path, res);
                path.pop_back();
            }
            if (n->right)
            {
                dfs(n->right, path, res);
                path.pop_back();
            }
        }
    };


class Solution {
    public:
        vector<string> binaryTreePaths(TreeNode* root) {
            vector<string> res;
            array<TreeNode*, 105> stk;
            int top = -1;
            TreeNode* p = root;
            TreeNode* pre = new TreeNode(0);
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
                        if (!tmp->left && !tmp->right)
                        {
                            string s;
                            for (int i = 0; i <= top; i ++ )
                            {
                                s += to_string(stk[i]->val);
                                s += "->";
                            }
                            res.push_back(s.substr(0, s.size() - 2));
                        }
                        pre = tmp;
                        top --;
                    }
                }
            }
            return res;
        }
    };