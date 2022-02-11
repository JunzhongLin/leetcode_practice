'''

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
'''


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.arrayBucket = [Bucket() for i in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.arrayBucket[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.arrayBucket[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.arrayBucket[bucket_index].exists(key)


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class Bucket:
    def __init__(self, ):
        self.head = Node(0)

    def insert(self, val):

        if not self.exists(val):
            newNode = Node(val, next_node=self.head.next)
            self.head.next = newNode

    def delete(self, val):
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, val):

        if self.head.next:

            curr = self.head.next
            while curr:
                if curr.val == val:
                    return True
                curr = curr.next
        return False