'''
Write a Python program to calculate the sum of a list of numbers.

'''

class Solution:
    def sum_list(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + self.sum_list(nums[1:])

if __name__ == '__main__':
    nums_list = [1,2,3,4]
    res = Solution().sum_list(nums_list)

    '''
 func([1,2,3,4])    
    1 + func([2,3,4])
        2 + func([3,4])
            3 + func([4]) =4
    
    '''