/*
 * @lc app=leetcode.cn id=2410 lang=cpp
 *
 * [2410] 运动员和训练师的最大匹配数
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        ranges::sort(players);
        ranges::sort(trainers);
        int i = 0, j = 0, res = 0;
        while (i < players.size() && j < trainers.size())
        {
            if (players[i] <= trainers[j])
            {
                res ++, i ++, j ++;
            }
            else j ++;
        }
        return res;
    }
};
// @lc code=end

