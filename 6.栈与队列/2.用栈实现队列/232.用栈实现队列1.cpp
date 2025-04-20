/*
 * @lc app=leetcode.cn id=232 lang=cpp
 *
 * [232] 用栈实现队列
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class MyQueue {
public:
    stack<int> stk1, stk2;
    MyQueue() {

    }
    
    void push(int x) {
        stk1.push(x);
    }
    
    int pop() {
        if (stk2.size())
        {
            int res = stk2.top();
            stk2.pop();
            return res;
        }
        while (stk1.size())
        {
            stk2.push(stk1.top());
            stk1.pop();
        }
        int res = stk2.top();
        stk2.pop();
        return res;
    }
    
    int peek() {
        int tmp = this->pop();
        stk2.push(tmp);
        return tmp;
    }
    
    bool empty() {
        return stk1.empty() && stk2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end

