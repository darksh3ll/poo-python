class Student:
    def __init__(self,age):
        self.age = age

    def set_age(self,age):
        self.age = age


a = Student(12)
print(a.age)