class A:
    def __init__(self):
        print("This is class A")
    def fun1(self):
        print("This is Father Class")


class B(A):
    def __init__(self):
        print("This is class B")
        super().__init__()
    def fun2(self):
        print("This is Mother Class")

obj = B()

