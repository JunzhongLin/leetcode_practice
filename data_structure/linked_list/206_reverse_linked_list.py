'''

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            pre = cur
            cur = temp
        return pre

    def reverseList_recursive(self, head):

        def reverse(pre, cur):
            if not cur:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(cur, temp)

        return reverse(None, head)
