a = 1000

class Test:

    def func(self, a):
        self.a = a
        self.a += 2

Test().func(a)
