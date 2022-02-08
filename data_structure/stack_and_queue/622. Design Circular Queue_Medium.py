'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language.

'''


class MyCircularQueue:
    # Time complexity O(1)
    # Space complexity O(N)
    # May cause data

    def __init__(self, k: int):
        self.capacity = k
        self.head_index = 0
        self.que = [0] * k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False

        self.count += 1
        tail_index = (self.head_index + self.count - 1) % self.capacity
        self.que[tail_index] = value
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.que[self.head_index] = 0
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1

        return self.que[self.head_index]

    def Rear(self) -> int:
        if self.count == 0:
            return -1

        tail_index = (self.head_index + self.count - 1) % self.capacity
        print(tail_index, self.que)
        return self.que[tail_index]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.capacity:
            return True
        return False
