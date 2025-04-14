/*
 * @lc app=leetcode.cn id=225 lang=cpp
 *
 * [225] 用队列实现栈
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class MyStack {
public:
    MyStack() {
        
    }
    
    void push(int x) {
        q2.push(x);
        while (!q1.empty())
        {
            q2.push(q1.front());
            q1.pop();
        }
        swap(q1, q2);
    }
    
    int pop() {
        int res = q1.front();
        q1.pop();
        return res;
    }
    
    int top() {
        return q1.front();
    }
    
    bool empty() {
        return q1.empty();
    }
private:
    queue<int> q1;
    queue<int> q2;
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
class MyStack {
    public:
        MyStack() {
            
        }
        
        void push(int x) {
            q1.push(x);
        }
        
        int pop() {
            while (q1.size() > 1)
            {
                int tmp = q1.front();
                q1.pop();
                q2.push(tmp);
            }
            while (!q2.empty())
            {
                int tmp = q2.front();
                q2.pop();
                q1.push(tmp);
            }
            int res = q1.front();
            q1.pop();
            return res;
        }
        
        int top() {
            int res = this->pop();
            q1.push(res);
            return res;
        }
        
        bool empty() {
            return q1.empty();
        }
    private:
        queue<int> q1;
        queue<int> q2;
    };
    
