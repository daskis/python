from Shape import Shape


class C3(Shape):
    def __init__(self, x, y, param1, param2, param3):
        super().__init__(x, y)
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def square(self):
        return 0.5 * self.param1 * self.param2

    def perimeter(self):
        return self.param1 + self.param2 + self.param3

    def additionalMethod1(self):
        pass

    def additionalMethod2(self):
        pass
