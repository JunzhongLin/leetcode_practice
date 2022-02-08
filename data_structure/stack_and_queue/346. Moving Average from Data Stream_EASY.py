'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.


'''
import collections

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.que = collections.deque()

    def next(self, val: int) -> float:
        if len(self.que) < self.size:
            self.que.append(val)
        else:
            self.que.popleft()
            self.que.append(val)

        return sum(self.que) / len(self.que)