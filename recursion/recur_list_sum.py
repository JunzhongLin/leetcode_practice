'''
Write a Python program of recursion list sum. Go to the editor
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21

'''


class Solution:

    def recur_list_sum(self, nums):
        sum_res = 0
        for element in nums:
            if type(element) == type([]):
                sum_res += self.recur_list_sum(element)
            else:
                sum_res += element
        return sum_res

if __name__ == '__main__':
    nums_list = [1, 2, [3,4], [5,6]]
    res = Solution().recur_list_sum(nums_list)