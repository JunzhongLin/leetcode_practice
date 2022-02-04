'''
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

'''


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class SolutionTLE:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy_head, dummy_tail = Node(0, None, head, None), Node(0, None, None, None)
        curr = head
        prev = dummy_head

        if not head:
            return

        while curr:
            if curr.child:
                curr.next, curr.child = curr.child, curr.next
                curr.next.prev = curr

            prev = prev.next
            curr = curr.next

        prev.next, dummy_tail.prev = dummy_tail, prev
        curr = prev

        while curr:
            print(curr.val)
            if curr.child:
                dummy_tail.prev.next, curr.child.prev = curr.child, dummy_tail.prev
                temp_ptr = curr.child
                curr.child = None
                while temp_ptr.next:
                    temp_ptr = temp_ptr.next
                temp_ptr.next, dummy_tail.prev = dummy_tail, temp_ptr
            curr = curr.prev

        dummy_tail.prev.next = None

        return dummy_head.next


class Solution(object):
    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next