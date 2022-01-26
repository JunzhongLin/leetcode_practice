'''

Write a Python program to calculate the harmonic sum of n-1. Go to the editor
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example : 1+ 1/2 +1/3 .....

'''

class Solution:
    def harmonic_sum(self, num):
        if num == 1:
            return 1
        else:

            return 1/num + self.harmonic_sum(num-1)

if __name__ == '__main__':
    res = Solution().harmonic_sum(4)