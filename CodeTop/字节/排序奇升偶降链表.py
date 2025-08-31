from typing import Optional
import sys
class ListNode:
    def __init__(self, val = 0, nxt = None) -> None:
        self.val = val; self.nxt = nxt
    
def solve(head: Optional[ListNode]):
    if not head or not head.nxt: return head
    dummy2 = ListNode(nxt=head.nxt)
    up = head; down = head.nxt
    while down:
        up.nxt = down.nxt
        up = down
        down = up.nxt
    l1 = head
    pre = None
    cur = dummy2.nxt
    while cur:
        tmp = cur.nxt
        cur.nxt = pre
        pre = cur
        cur = tmp
    l2 = pre
    dummy = cur = ListNode()
    while l1 and l2:
        if l1.val > l2.val: cur.nxt = l2; l2 = l2.nxt
        else: cur.nxt = l1; l1 = l1.nxt
        cur = cur.nxt
    cur.nxt = l1 if l1 else l2
    return dummy.nxt

def main():
    dummy = cur = ListNode()
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        nums = list(map(int, line.split()))
    for x in nums:
        cur.nxt = ListNode(x)
        cur = cur.nxt
    h = solve(dummy.nxt)
        
if __name__ == "__main__":
    main()