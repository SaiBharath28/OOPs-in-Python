# Method over-riding
"""
same class
same function or method names
different parameters

"""

class A:
    def sum(self, a, b):
        return a+b
    def sum(self, a, b, c=1):
        return a+b+c
obj = A()
print(obj.sum(1,2))

print("----------")
print("----------")



# Method over-riding
"""

different classes
same function or method names
different parameters

"""

class X:
    def display(self):
        print("This is class A")
class Y(X):
    def display(self):
        print("This is class B")
        super().display()

obj = Y()
obj.display()