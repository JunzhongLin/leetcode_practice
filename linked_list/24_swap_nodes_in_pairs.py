'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head):
        dummy = ListNode(next=head)
        pre = dummy
        cur = head
        next = head.next
        while next.next:
            pre.next = next
            cur.next = next.next
            next.next = cur

            pre = cur
            cur = pre.next
            next = cur.next


        return dummy.next