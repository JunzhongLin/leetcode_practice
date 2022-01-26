'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next
 is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate
the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
 the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index
 equals the length of the linked list, the node will be appended to the end of the linked list. If index
 is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

'''


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class LinkNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self, val=0, next=None):
        self._head = LinkNode()
        self._count = 0

    def get(self, index: int) -> int:
        """
           Get the value of the index-th node in the linked list. If the index is invalid, return -1.
           """
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val):

        return self.addAtIndex(0, val)

    def addAtTail(self, val):
        return self.addAtIndex(self._count, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return None

        self._count += 1
        previous_node, current_node = None, self._head
        add_node = LinkNode(val)
        for _ in range(index+1):
            previous_node, current_node = current_node, current_node.next
        else:
            previous_node.next, add_node.next = add_node, current_node

    def deleteAtIndex(self, index: int) -> None:
        if 0< index < self._count:
            previous_node, current_node = None, self._head
            self._count -= 1
            for _ in range(index+1):
                previous_node, current_node = current_node, current_node.next
            previous_node.next, current_node.next = current_node.next, None
        else:
            return


class d_Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyDoubleLinkedNodes:
    def __init__(self):
        self._head, self._tail = d_Node(0), d_Node(0)
        self._head.next, self._tail.prev = self._tail, self._head
        self._count = 0

    def _get_node(self, index):
        if index >= self._count//2:
            cur = self._tail
            for _ in range(self._count-index):
                cur = cur.prev
        else:
            cur = self._head
            for _ in range(index+1):
                cur = cur.next

        return cur

    def get(self, index: int) -> int:
        if  0< index < self._count:
            current_node = self._get_node(index)
            return current_node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._update(self._head, self._head.next, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self._update(self._tail.prev, self._tail, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._update(node.prev, node.next, val)

    def _update(self, prev, next, val):
        self._count += 1
        add_node = d_Node(val)
        prev.next, add_node.prev, add_node.next, next.prev = add_node, prev, next, add_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._count:
            node = self._get_node(index)
            # 计数-1
            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev
