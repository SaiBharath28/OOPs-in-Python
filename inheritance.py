# single inheritance
class Parent:
    def fun1(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is child class")
obj = Child()
obj.fun2()
obj.fun1()

print("---------------")

# multi-level inheritance
class Parent:
    def fun1(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is child class")

class GrandChild(Child):
    def fun3(self):
        print("This is Grand child")
obj = GrandChild()
obj.fun3()
obj.fun2()
obj.fun1()

print("---------------")

# hierarchical inheritance
class Parent:
    def fun1(self):
        print("This is parent class")
class Child1(Parent):
    def fun2(self):
        print("This is child1 class")

class Child2(Parent):
    def fun3(self):
        print("This is Child2 Class")

obj1 = Child1()
obj1.fun1()
obj1.fun2()


print(" ")

obj2 = Child2()
obj2.fun1()
obj2.fun3()

print("---------------")


# Multiple inheritance
class Father:
    def fun1(self):
        print("This is Father Class")
class Mother:
    def fun2(self):
        print("This is Mother Class")

class Child(Father, Mother):
    def fun3(self):
        print("This is Child Class")
obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()