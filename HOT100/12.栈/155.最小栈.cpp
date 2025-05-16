/*
 * @lc app=leetcode.cn id=155 lang=cpp
 *
 * [155] 最小栈
 */
#include "tools.h"

// @lc code=start
class MinStack {
    stack<pair<int, int>> stk;
public:
    MinStack() {
        stk.emplace(0, INT_MAX);
    }
    
    void push(int val) {
        stk.emplace(val, min(getMin(), val));
    }
    
    void pop() {
        stk.pop();
    }
    
    int top() {
        return stk.top().first;
    }
    
    int getMin() {
        return stk.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
// @lc code=end

