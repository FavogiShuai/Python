class A:
    def __init__(self):
        self.__p1 = 100

    def __m1(self):
        print('m1 function')
        pass

    def test(self):
        print(self.__p1)
        self.__m1()
a = A()
# a.__p1  类外无法调用
print(a.test())
