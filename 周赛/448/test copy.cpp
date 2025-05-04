#include <bits/stdc++.h>
using namespace std;
class Solution {
    public:
        int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
            
            for (int i = 0; i < k; i ++ )
            {
                int maxDiff = INT_MIN;
                int maxIdx = -1;
                for (int i = 0; i < n - 1; i ++ )
                {
                    if ((position[i + 1] - position[i]) * time[i] > maxDiff)
                    {
                        maxDiff = (position[i + 1] - position[i]) * time[i];
                        maxIdx = i;
                    }
                }
                position.erase(position.begin() + maxIdx);
                time[maxIdx + 1] += time[maxIdx];
                time.erase(time.begin() + maxIdx);
            }
            int res = 0;
            for (int i = 0; i < n - 1; i ++ )
            {
                res += (position[i + 1] - position[i]) * time[i];
            }
            return res;
        }
    };