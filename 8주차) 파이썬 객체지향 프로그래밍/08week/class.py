################################################################
# 클래스를 이용한 구현의 예

# 함수를 이용한 구현
def add(x, y):
    return x + y

val_x = 1
val_y = 2
val_sum = add(val_x, val_y)
print(val_sum)

# 클래스를 이용한 구현
class Calc:
    name = 'Calc'
    def __init__(self):
        self.value = 0                 

    def add(self, x, y):
        self.value = x + y
        return self.value
        
    def getLastValue(self):
        return self.value        

myCalc = Calc()
print(type(myCalc))
yourCalc = Calc()

print(myCalc.add(1, 2))
print(yourCalc.add(3, 4))

print(myCalc.getLastValue())
print(yourCalc.getLastValue())

print(myCalc.value)
print(yourCalc.value)

print(Calc.getLastValue(myCalc))
print(Calc.getLastValue(yourCalc))

print(Calc.name)
print(myCalc.name)
print(yourCalc.name)

myCalc.name = 'MyCalc'
print(Calc.name)
print(myCalc.name)
print(yourCalc.name)

Calc.name = 'Class - Calc'
print(Calc.name)
print(myCalc.name)
print(yourCalc.name)

################################################################
# 클래스 변수 (static변수) 의 사용예
class exClass:
	staticVar = 0

	def __init__(self):
		exClass.staticVar += 1
		self.var = exClass.staticVar

obj1 = exClass()
print(obj1.var) 

obj2 = exClass()
print(obj2.var)

print(exClass.staticVar) 

################################################################
# 클래스 상속, 오버라이딩의 구현
class Animal:
    def __init__(self):
        self._name = 'Animal'
        self.age = 0

    def __str__(self):
        return 'name: ' + self._name + ', age: ' + str(self.age)

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age
        
    def say(self):
        print('Animal Hello')
    
animal = Animal()
print(animal)

animal.setName('MyAnima')
print(animal.getName())
print(animal._name)

animal.setAge(10)
print(animal.getAge())
animal.say()

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Dog'
        self.age = 10
        
dog = Dog()
print(dog)
dog.say()

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Cat'
        self.age = 20
        
    def say(self, message):
        super().say()
        print('Cat ' + message)
        
cat = Cat()
print(cat)
cat.say('Hi~~~')
