class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showInfo(self):
        print("부모")
        print("이름 : ",self.name)
        print("나이 :",self.age)

class Student(Person):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number = number

s = Student("pika",10,2020123)
s.showInfo()