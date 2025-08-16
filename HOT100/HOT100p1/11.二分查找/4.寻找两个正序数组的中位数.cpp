/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto find = [&](auto&& self, vector<int>& n1, int i, vector<int>& n2, int j, int k) -> int
        {
            if (n1.size() - i > n2.size() - j)
            {
                return self(self, n2, j, n1, i, k);
            }
            if (i == n1.size())
            {
                return n2[j + k - 1];
            }
            if (k == 1)
            {
                return min(n1[i], n2[j]);
            }
            int idx1 = min((int)n1.size(), i + k / 2);
            int idx2 = j + k - k / 2;
            if (n1[idx1 - 1] > n2[idx2 - 1])
            {
                return self(self, n1, i, n2, idx2, k - (idx2 - j));
            }
            else
            {
                return self(self, n1, idx1, n2, j, k - (idx1 - i));
            }
        };
        int n = nums1.size() + nums2.size();
        if (n % 2)
        {
            return (double)find(find, nums1, 0, nums2, 0, n / 2 + 1);
        }
        else
        {
            int l = find(find, nums1, 0, nums2, 0, n / 2);
            int r = find(find, nums1, 0, nums2, 0, n / 2 + 1);
            return (l + r) / 2.0;
        }
    }
};
// @lc code=end

