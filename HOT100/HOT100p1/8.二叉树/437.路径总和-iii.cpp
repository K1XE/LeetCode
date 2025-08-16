/*
 * @lc app=leetcode.cn id=437 lang=cpp
 *
 * [437] 路径总和 III
 */
#include "tools.h"
using namespace std;
struct TreeNode
{
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
    int res = 0;
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, long long> hash;
        hash[0] = 1;
        auto dfs = [&](auto&& self, TreeNode* n, long long val) -> void
        {
            if (! n) return;
            val += n->val;
            res += hash[val - targetSum];
            hash[val] += 1;
            self(self, n->left, val);
            self(self, n->right, val);
            hash[val] -= 1;
        };
        dfs(dfs, root, 0);
        return res;
    }
};
// @lc code=end

