class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

root = lst2link([1,2,3,4,5,6])
