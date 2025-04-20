/*
 * @lc app=leetcode.cn id=225 lang=cpp
 *
 * [225] 用队列实现栈
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;

// @lc code=start
class MyStack {
public:
    queue<int> q1, q2;
    MyStack() {
        
    }
    
    void push(int x) {
        q1.push(x);
        while (q2.size())
        {
            q1.push(q2.front());
            q2.pop();
        }
        swap(q1, q2);
    }
    
    int pop() {
        int res = q2.front();
        q2.pop();
        return res;
    }
    
    int top() {
        int res = this->pop();
        this->push(res);
        return res;
    }
    
    bool empty() {
        return q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
// @lc code=end

