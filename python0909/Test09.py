#import
import random

#0~1사이 난수
num1 = random.random()
print(num1)

num2 = random.randint(1,5)
print(num2)
#choice
lst = [10,20,30,40,50]
num3 = random.choice(lst)
print(num3)
#sample
num4 = random.sample(lst,3)
print(num4)
#shuffle
random.shuffle(lst)
print(lst)
