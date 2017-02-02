class A:

    def __init__(self, a):
        self.__a = a

    def method(self):
        print('class A', self.__a)


class B:
    def __init__(self, b):
        self.__b = b

    def method(self):
        print('class B', self.__b)


class C(A, B):

    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.__c = c

    def method(self):
        print('class C', self.__c)

    def test_super_methods(self):
        A.method(self)
        B.method(self)
        self.method()


c = C('a', 'b', 'c')
c.test_super_methods()
