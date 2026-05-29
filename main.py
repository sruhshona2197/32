 69. Polymorphism
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

for obj in [Car(), Plane()]:
    print(obj.move())


# 70. Nested Class
class University:
    class Student:
        def info(self):
            return "Student info"

s = University.Student()
print(s.info())


# 71. Getter & Setter
class Temperature:
    def __init__(self):
        self.__temp = 0

    def set_temp(self, t):
        self.__temp = t

    def get_temp(self):
        return self.__temp

t = Temperature()
t.set_temp(36)
print(t.get_temp())


# 72. Dynamic Attribute
class Person:
    pass

p = Person()
p.name = "Ali"
print(p.name)
