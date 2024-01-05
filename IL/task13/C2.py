from Shape import Shape


class C2(Shape):
    def __init__(self, x, y, param1):
        super().__init__(x, y)
        self.param1 = param1

    def square(self):
        return self.param1 ** 2

    def perimeter(self):
        return 4 * self.param1

    def additionalMethod1(self):
        pass

    def additionalMethod2(self):
        pass