'''

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
'''


class TwoSum:

    def __init__(self):
        self.nums = []
        self.size = 0

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.size += 1

    def find(self, value: int) -> bool:
        hash_map = {}
        for i in range(self.size):
            hash_map[value - self.nums[i]] = i

        for i in range(self.size):
            if self.nums[i] in hash_map and hash_map[self.nums[i]] != i:
                return True
        return False