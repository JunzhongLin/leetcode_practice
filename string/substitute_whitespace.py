'''

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
'''


class Solution:
    def replaceSpace(self, s):
        res = list(s)
        space_counts = res.count(' ')
        res.extend([' '] *space_counts * 2)

        left, right = len(s)-1, len(res)-1
        while left>=0:
            # print(res, res[left], left)
            if res[left] != ' ':
                res[right] = res[left]
                left -= 1
                right -= 1
            elif res[left] == ' ':
                res[right-2:right+1] = list('%20')
                left -= 1
                right -= 3

        return ''.join(res)

if __name__ == '__main__':
    s = 'this is a test'
    res= Solution().replaceSpace(s)