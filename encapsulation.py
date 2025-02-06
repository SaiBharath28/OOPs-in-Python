"""

wrapping of variables and methods in single unit
access specifiers :
public,
private __,
protected _

"""
class Demo():
    def __init__(self, a, b):

        self.__a = a  # private
        self._b = b  # protected

class Demo2(Demo):
    def output(self):
        print(self._b)

d = Demo2(3,4)
d.output()