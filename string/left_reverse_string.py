'''
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，
输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

 

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

'abcdefg' k=2
'bagfedc'
'cdefgab'

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
'''


class Solution:
    def reverseLeftWords(self, s, n):

        def reverse_sub(sub_s):
            left, right = 0, len(sub_s)-1
            while left < right:
                sub_s[left], sub_s[right] = sub_s[right], sub_s[left]
                left += 1
                right -= 1
            return sub_s
        res = list(s)
        res[:n] = reverse_sub(res[:n])
        res[n:] = reverse_sub(res[n:])
        res = reverse_sub(res)
        return ''.join(res)


if __name__ == '__main__':
    s = 'abcdef'
    n =2
    res = Solution().reverseLeftWords(s,2
                                      )