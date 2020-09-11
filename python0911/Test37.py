class Character:
    count = 0
    def __init__(self,name):
        self.name = name
        print("%s가 만들어지는중....." %self.name)
        Character.count +=1
    def die(self):
        print("%s가 죽었습니다....." % self.name)
        Character.count += 1
    def info(self):
        print("현재 살아있는 캐릭터의 수는 %d 이다" %Character.count)

elf1 = Character("엘프1")
elf2 = Character("엘프2")
elf3 = Character("엘프3")
elf1.info()