
"""
Given ordered sequence of integers your task is to represent this sequence as a sequence of either ranges or
individual integers in the same order as initial sequence.

Range is a sequence of 3 or more consequitive numbers including both endpoints.

It is guaranteed that sequence does not have repeated values.

For example:

[12, 13,  15, 16, 17 ] ->
[12, 13, (15,     17)]


[-6,  -3, -2, -1, 0, 1 ,  3, 4, 5 ,  7, 8, 9, 10, 11 , 14, 15,  17, 18, 19, 20 ] ->
[-6, (-3,            1), (3,    5), (7,           11), 14, 15, (17,         20)]

"""


class Solution:
#
#     def gen_seq(self, num_list):
#
#         res = []
#         temp = []
#         i = 0
#         if len(num_list) <= 2:
#             return num_list
#
#         while i <= len(num_list) - 3:
#
#             if num_list[i + 2] != num_list[i] + 2:
#                 res.append(num_list[i])
#                 i += 1
#
#             else:
#
#                 temp = []
#                 while i <= len(num_list) - 3 and (num_list[i + 2] == num_list[i] + 2):
#                     temp.append(num_list[i])
#                     i += 1
#
#                 temp.append(num_list[i + 1])
#
#                 i += 2
#
#                 res.append(tuple([temp[0], temp[-1]]))
#
#         return res
#
    def gen_seq_2(self, num_list):

        res = []
        slow, fast = num_list[0], num_list[0]
        for num in num_list[1:]+['a']:
            if num != fast+1:
                if fast == slow:
                    res.append(slow)
                elif fast == slow+1:
                    res += [slow, fast]
                else: res.append(tuple([slow, fast]))
                slow = num
            fast = num
        return res

    def gen_seq_3(self, num_list):

        res = []
        que = []
        que.append(num_list[0])

        for num in num_list[1:]+['a']:

            if num != que[-1]+1:

                if len(que) == 1:
                    res.append(que.pop(0))
                elif len(que) == 2:
                    res.append(que.pop(0))
                    res.append(que.pop(0))
                else:
                    res.append(tuple([que.pop(0), que.pop(-1)]))
                    que.clear()

            que.append(num)

        return res





#
#     def gen_seq_3(self, num_list):
#         import collections
#         diff = [num_list[i+1] - num_list[i] for i in range(len(num_list)-1)]
#         que = collections.deque()
#         res = []
#         i=0
#         while i <= len(num_list):
#             que.append(num_list[i])
#
#             if diff[i] != 1:
#                 res.append(que.popleft())
#                 i += 1
#
#             elif diff[i] == 1:
#                 # que.append(num_list[i])
#                 que.append(num_list[i+1])
#                 i += 1
#                 while i < len(diff)-2 and diff[i] == 1:
#                     que.append(num_list[i+1])
#                     i += 1
#                 if diff[i] !=1 or i==len(diff)-1:
#                     res.append(tuple([que.popleft(), que.pop()]))
#                     que.clear()
#                     i += 1
#         return res
#
#    def gen_seq_4(self, num_list):
#        from itertools import groupby
#        diff = [num_list[i+1] - num_list[i] for i in range(len(num_list)-1)]
#        index = 0
#        res = []
#        for k, g in groupby(diff, key=lambda x: x==1):
#            len_ = len(list(g))
#            if k == 0 and index == 0:
#                res += num_list[:index+len_]
#            elif k == 0 and len_ > 2 and index != 0:
#                res += num_list[index+1: index+len_]
#            elif k == 0 and len_< 2 and index != 0:
#                index += len_
#                continue
#                # res += [tuple([num_list[index-1], num_list[index-1+len(list(g))]])]
#            elif k == 1 and len_ >= 2 and index != 0:
#                res += [tuple([num_list[index], num_list[index+ len_]])]
#            elif k ==1 and len_ < 2 and index!= 0:
#                res += num_list[index: index+len_+1]
#            elif k == 1 and index == 0 and len_ < 2:
#                res += num_list[:index]
#            print('length:', len_, 'index:', index, k, res)
#
#            index += len_
#
#        return res

class Solution_2:
    def gen_seq(self, num_list):
        from itertools import groupby
        diff = [num_list[i+1] - num_list[i] for i in range(len(num_list)-1)]
        index = 0
        res = []
        for k, g in groupby(diff, key=lambda x: x==1):
            len_ = len(list(g))
            if k == 0 and index == 0:
                res += num_list[:index+len_]
            elif k == 0 and len_ >= 2 and index != 0:
                res += num_list[index+1: index+len_+1]
            elif k == 0 and len_< 2 and index != 0 and index != len(diff)-1:
                index += len_
                continue
            elif k == 0 and len_< 2 and index == len(diff)-1:
                res += num_list[index+1:]
                # res += [tuple([num_list[index-1], num_list[index-1+len(list(g))]])]
            elif k == 1 and len_ >= 2 and index != 0:
                res += [tuple([num_list[index], num_list[index+ len_]])]
            elif k ==1 and len_ < 2 and index!= 0:
                res += num_list[index: index+len_+1]
            elif k == 1 and index == 0 and len_ < 2:
                res += num_list[:index]
            print('length:', len_, 'index:', index, k, res)

            index += len_

        return res



'''
    a = [-6,  -3, -2, -1, 0, 1 ,  3, 4, 5,  7, 8, 9, 10, 11 , 14, 15,  17, 18, 19, 20 , 22]

   0  1  2  3  4  5  6
  -6 -3 -2

'''


def solution(args):
    out = []
    beg = end = args[0]
    i=0

    for n in args[1:] + [""]:
        print('round:', i, '!!', n, 'end:', end, 'begin:', beg)
        i+=1
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)



if __name__ == '__main__':
    a = [-6,  -3, -2, -1, 0, 1 ,  3, 4, 5,  7, 8, 9, 10, 11 , 14, 15,  17, 18, 19, 20, 21, 25, 27, 28, 29]
    b= [3, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 2, 2, 2, 1]
    diff = [a[i+1]-a[i] for i in range(len(a)-1)]
    res = Solution().gen_seq_3(a)
    print(res)


