/*
 * @lc app=leetcode.cn id=3362 lang=cpp
 *
 * [3362] 零数组变换 III
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int sums_d = 0, j = 0;
        ranges::sort(queries);
        int n = nums.size();
        vector<int> diff(n, 0);
        priority_queue<int> heap;
        for (int i = 0; i < n; i ++ )
        {
            sums_d += diff[i];
            while (j < queries.size() && queries[j][0] <= i)
            {
                heap.push(queries[j][1]);
                j ++;
            }
            while (sums_d + nums[i] > 0 && heap.size() && heap.top() >= i)
            {
                sums_d --;
                int r = heap.top();
                heap.pop();
                if (r + 1 < n) diff[r + 1] ++;
            }
            if (sums_d + nums[i] > 0) return -1;
        }
        return heap.size();
    }
};
// @lc code=end

