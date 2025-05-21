/*
 * @lc app=leetcode.cn id=295 lang=cpp
 *
 * [295] 数据流的中位数
 */
#include "tools.h"
// @lc code=start
class MedianFinder {
public:
    priority_queue<int> left;
    priority_queue<int, vector<int>, greater<>> right;
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (left.size() == right.size())
        {
            right.push(num);
            left.push(right.top());
            right.pop();
        }
        else
        {
            left.push(num);
            right.push(left.top());
            left.pop();
        }
    }
    
    double findMedian() {
        if (left.size() > right.size()) return left.top();
        else return (left.top() + right.top()) / 2.0f;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
// @lc code=end

