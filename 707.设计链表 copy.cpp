/*
 * @lc app=leetcode.cn id=707 lang=cpp
 *
 * [707] 设计链表
 */

// @lc code=start
class MyLinkedList {
    public:
        struct ListNode{
            int val;
            ListNode* next;
            ListNode* pre;
            ListNode(int x) : val(x), next(nullptr) {}
        };
        MyLinkedList() {
            dummyHead = new ListNode(0);
            dummyHead->next = nullptr;
            dummyHead->pre = nullptr;
            _size = 0;
        }
        
        int get(int index) {
            if (index >= _size) return -1;
            ListNode* p = dummyHead->next;
            p->pre = dummyHead;
            while (index --)
                p = p->next;
            return p->val;
        }   
        
        void addAtHead(int val) {
            addAtIndex(0, val);
        }
        
        void addAtTail(int val) {
            addAtIndex(_size, val);
        }
        
        void addAtIndex(int index, int val) {
            if (index > _size) return;
            ListNode* prev = dummyHead;
            
            while (index --)
                prev = prev->next;
            ListNode* newp = new ListNode(val);
            newp->next = prev->next;
            newp->pre = prev;
            prev->next = newp;
            if (newp->next)
                newp->next->pre = newp;
            _size ++;
            return;
        }
        
        void deleteAtIndex(int index) {
            if (index >= _size) return;
            ListNode* p = dummyHead->next;
            p->pre = dummyHead;
            while (index --)
                p = p->next;
            ListNode* prev = p->pre;
            prev->next = p->next;
            if (p->next)
                p->next->pre = prev;
            _size --;
            return;
        }
    private:
        ListNode* dummyHead;
        int _size;
    };
    
    /**
     * Your MyLinkedList object will be instantiated and called as such:
     * MyLinkedList* obj = new MyLinkedList();
     * int param_1 = obj->get(index);
     * obj->addAtHead(val);
     * obj->addAtTail(val);
     * obj->addAtIndex(index,val);
     * obj->deleteAtIndex(index);
     */
// @lc code=end
