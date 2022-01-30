'''
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val,
and return the new head.

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_element(self, head, target):
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while not cur.next:
            if cur.next.val == target:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next
