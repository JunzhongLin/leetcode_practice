'''
Write a Python program to get the factorial of a non-negative integer.

'''


class Solution:
    def __init__(self, num):
        self.num = num
        self.res = []

    def factor_int_loop(self,):
        res_list= []
        for i in range(1, self.num+1):
            if self.num % i == 0:
                res_list.append(i)
        return res_list

    def factor_int(self, x):
        if x == 1:
            self.res.append(x)
        elif self.num % x == 0:
            self.res.append(x)
            self.factor_int(x-1)
        else:
            self.factor_int(x-1)
        return self.res

    def factor_int_2(self, x):
        res = []

        if x == 1:
            res.append(x)
            return res
        elif self.num % x == 0:

            return res + [x] + self.factor_int(x-1)
        else:
            return res + self.factor_int(x-1)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))


def factors(x):
    if x == 1:
        print(1 ,end =" ")
    elif num % x == 0:
        factors(x-1)
        print(x, end =" ")
    else:
        factors(x-1)



if __name__ == '__main__':
    num = 6
    res = Solution(18).factor_int_2(18)

    # x = num = int(input('Enter an integer: '))
    # print('The factors of', x, 'are: ', end=" ")
    # factors(x)