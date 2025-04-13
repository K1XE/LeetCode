/*
 * @lc app=leetcode.cn id=707 lang=cpp
 *
 * [707] 设计链表
 */

// @lc code=start
class MyLinkedList {
    public:
        struct LinkList
        {
            LinkList* next;
            int val;
        };
        
        MyLinkedList() {
            _dummyhead = new LinkList();
            _dummyhead->next = nullptr;
            _size = 0;
        }
        
        int get(int index) {
            LinkList* p = _dummyhead->next;
            int len = 0;
            while (p)
            {
                len ++;
                p = p->next;
            }
            if (index >= len) return -1;
            LinkList* q = _dummyhead->next;
            while (index)
            {
                q = q->next;
                index --;
            }
            return q->val;
        }
        
        void addAtHead(int val) {
            LinkList* p = new LinkList();
            p->next = _dummyhead->next;
            p->val = val;
            _dummyhead->next = p;
            _size ++;
        }
        
        void addAtTail(int val) {
            LinkList* p = _dummyhead;
            while (p->next != nullptr)
            {
                p = p->next;
            }
            LinkList* q = new LinkList();
            p->next = q;
            q->next = nullptr;
            q->val = val;
            _size ++;
        }
        
        void addAtIndex(int index, int val) {
            LinkList* p = _dummyhead->next;
            int len = 0;
            while (p)
            {
                len ++;
                p = p->next;
            }
            if (index > len) return;
            LinkList* cur = _dummyhead->next;
            LinkList* pre = _dummyhead;
            int cnt = 0;
            while (cnt != index)
            {
                pre = cur;
                cur = cur->next;
                cnt ++;
            }
            LinkList* t = new LinkList();
            t->val = val;
            t->next = pre->next;
            pre->next = t;
            _size ++;
            return;
        }
        
        void deleteAtIndex(int index) {
            LinkList* p = _dummyhead->next;
            int len = 0;
            while (p)
            {
                len ++;
                p = p->next;
            }
            if (index >= len) return;
            LinkList* cur = _dummyhead->next;
            LinkList* pre = _dummyhead;
            while (index)
            {
                pre = cur;
                cur = cur->next;
                index --;
            }
            LinkList* tmp = pre->next;
            pre->next = cur->next;
            delete tmp;
            tmp = nullptr;
            _size --;
            return;
        }
    private:
        LinkList* _dummyhead;
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
class MyLinkedList {
    public:
        struct LinkList{
            int val;
            LinkList* next;
            LinkList* prev;
            LinkList(int x) : val(x), next(nullptr), prev(nullptr) {}
        };
        MyLinkedList() {
            _dummyhead = new LinkList(0);
            _size = 0;
        }
        
        int get(int index) {
            if (index > _size - 1) return -1;
            LinkList* cur = _dummyhead->next;
            while (index -- )
            {
                cur = cur->next;
            }
            return cur->val;
        }
        
        void addAtHead(int val) {
            addAtIndex(0, val);
        }
        
        void addAtTail(int val) {
            addAtIndex(_size, val);
        }
        
        void addAtIndex(int index, int val) {
            if (index > _size) return;
            LinkList* pre = _dummyhead;
            LinkList* cur = pre->next;
            while (index -- )
            {
                pre = cur;
                cur = cur->next;
            }
            LinkList* tmp = new LinkList(val);
            tmp->next = cur;
            tmp->prev = pre;
            pre->next = tmp;
            if (cur)
            {
                cur->prev = tmp;
            }
            _size ++;
            return;
        }
        
        void deleteAtIndex(int index) {
            if (index > _size - 1) return;
            LinkList* pre = _dummyhead;
            LinkList* cur = pre->next;
            while (index -- )
            {
                pre = cur;
                cur = cur->next;
            }
            pre->next = cur->next;
            if (cur->next)
            {
                cur->next->prev = pre;
            }
            delete cur;
            _size --;
            return;
    
        }
    private:
        LinkList* _dummyhead;
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
