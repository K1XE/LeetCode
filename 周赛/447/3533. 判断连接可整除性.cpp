#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        vector<int> concatenatedDivisibility(vector<int>& nums, int k) {
            ranges::sort(nums);
            vector<int> res;
            do
            {
                if (f(nums, k))
                {
                    for (auto x : nums) res.push_back(x);
                    return res;
                }
            } while (next_permutation(nums.begin(), nums.end()));
            return res;
        }
        bool f(vector<int>& nums, int k)
        {
            long long tmp = 0;
            long long s = 0;
            for (int i = nums.size() - 1; i >= 0; i -- )
            {
                int d = 0;
                if (i < nums.size() - 1) d = get_d(nums[i + 1]);
                s += d;
                tmp += (long long)nums[i] * pow(10, s);
            }
            return tmp % k == 0 ? 1 : 0;
        }
        int get_d(int x)
        {
            int d = 0;
            while (x)
            {
                d ++;
                x /= 10;
            }
            return d;
        }
    };
int main()
{
    Solution sol;
    vector<int> nums = {1,4,6};
    int k = 8;
    sol.concatenatedDivisibility(nums, k);
    return 1;
}