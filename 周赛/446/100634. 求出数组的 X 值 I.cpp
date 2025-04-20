#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        vector<long long> resultArray(vector<int>& nums, int k) {
            vector<long long> pre(k);
            vector<long long> res(k);
            for (auto x : nums)
            {
                int mod = x % k;
                vector<long long> cur(k);
                for (int r = 0; r < k; r ++ )
                {
                    if (pre[r] == 0) continue;
                    int nr = (mod * r) % k;
                    cur[nr] += pre[r];
                }
                cur[mod] ++;
                for (int r = 0; r < k; r ++ )
                {
                    res[r] += cur[r];
                }
                pre = cur;
            }
            return res;
        }
    };

    class Solution {
    public:
        vector<long long> resultArray(vector<int>& nums, int k) {
            vector<__int128_t> pre(nums.size());
            vector<long long> res(k);
            pre[0] = nums[0];
            for (int i = 1; i < nums.size(); i ++ )
            {
                pre[i] = (__int128_t)pre[i - 1] * nums[i];
            }
            for (int i = 0; i < nums.size(); i ++ )
            {
                for (int j = nums.size() - 1; j >= 0; j --)
                {
                    if (j - i >= 0)
                    {
                        long long tmp;
                        if (i == 0) tmp = pre[j];
                        else tmp = (__int128_t)pre[j] / pre[i - 1];
                        long long r = tmp % k;
                        res[r] ++;
                    }
                }
            }
            return res;
        }
    };