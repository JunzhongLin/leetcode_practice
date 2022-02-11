'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


'''


class MyHashMap:

    def __init__(self):
        self.key_range = 791
        self.buckets_array = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        self.buckets_array[bucket_index].insert(key, value)

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        node = self.buckets_array[bucket_index].exists(key)
        print(node)
        if node:
            return node.val
        return -1

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.buckets_array[bucket_index].delete(key)


class Node:
    def __init__(self, key, val=0, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node


class Bucket:
    def __init__(self, ):
        self.head = Node(0)

    def insert(self, key, val):
        curr = self.exists(key)
        if not self.exists(key):
            newNode = Node(key, val, next_node=self.head.next)
            self.head.next = newNode
        else:
            curr.val = val

    def delete(self, key):
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def update(self, key, val):
        pass

    def exists(self, key):
        curr = None

        if self.head.next:
            curr = self.head.next
            while curr:
                if curr.key == key:
                    return curr
                curr = curr.next
        return curr

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)