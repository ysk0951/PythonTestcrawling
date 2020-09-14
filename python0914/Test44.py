#객체의 구조화

class Person:
    hp = 1
    itemCount = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print("걷기")
    def eat(self):
        print("먹기")
    def setIten(self):
        pass

#------------------------------------------------------
class Monster(Person):
    #생성자 오버라이딩
    def __init__(self,name,age,*args,**kwargs):
        super().__init__(name,age)
        for i in args:
            print(i)
        for i,j in kwargs.items():
            setattr(self,i,j)
            print(getattr(self,i))
        
            

class Elf(Person):
    pass

monster1 = Monster("monster1",10)

lst = list()
for i in range(50):
    lst.append(Monster("monster"+str(i+1),10+i,attack="10"))

print(lst[1].name)
print(lst[1].attack)

npc = dict()
for i in range(3):
    lst = list()
    for i in range(50):
        lst.append(Monster("monster"+str(i+1),10+i,attack=10))
    npc.update({"monster1"+str(i+1):lst})


