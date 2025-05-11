#include "tools.h"
using namespace std;
class Solution {
    public:
        bool canPartitionGrid(vector<vector<int>>& grid) {
            int m = grid.size(), n = grid[0].size();
            vector<long long> sumh(m, 0), suml(n, 0);
            
            for (int i = 0; i < m; i ++ )
            {
                for (int j = 0; j < n; j ++ )
                {
                    sumh[i] = (long long)sumh[i] + grid[i][j];
                }
            }
            for (int j = 0; j < n; j ++ )
            {
                for (int i = 0; i < m; i ++ )
                {
                    suml[j] = (long long)suml[j] + grid[i][j];
                }
            }
            for (int i = 1; i < m; i ++ )
            {
                sumh[i] = (long long)sumh[i] + sumh[i - 1];
            }
            for (int j = 1; j < n; j ++ )
            {
                suml[j] = (long long)suml[j] + suml[j - 1];
            }
            for (int i = 0; i < m; i ++ )
            {
                long long half1 = sumh[i];
                long long half2 = sumh.back() - sumh[i];
                if (half1 == half2) return 1;
            }
            for (int j = 0; j < n; j ++ )
            {
                long long half1 = suml[j];
                long long half2 = suml.back() - suml[j];
                if (half1 == half2) return 1;
            }
            return 0;
        }
    };