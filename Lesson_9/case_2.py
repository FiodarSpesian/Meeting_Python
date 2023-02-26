"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""


class MyMeto(type):
    el = None

    def __call__(self, *args, **kwargs):
        if self.el == None:
            return self.el


class TestClass(metaclass=MyMeto):

    def function(self):
        pass


a = TestClass()
b = TestClass()
c = TestClass()
d = TestClass()
print(a is b)
print(a is d)
print(c is d)
