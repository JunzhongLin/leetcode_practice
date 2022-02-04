'''
Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        dummy_head = Node(-1, next=head)
        in_node = Node(insertVal, None)

        if not head:
            head = in_node
            head.next = head
            return head

        elif head.next == head:
            in_node.next = head
            head.next = in_node
            return head

        prev, curr = head, head.next

        while curr:

            # print(prev.val, insertVal, curr.val)
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                prev.next = in_node
                in_node.next = curr
                return head
            elif prev.val <= insertVal <= curr.val:
                prev.next = in_node
                in_node.next = curr
                return head

            prev, curr = curr, curr.next

            if curr == head.next:
                break

        prev.next = in_node
        in_node.next = curr

        return head