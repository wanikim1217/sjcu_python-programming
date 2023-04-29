#---------------------------------------------------------------------------
"""
# 파이썬 객체지향 프로그래밍: 클래스를 이용한 구현의 예
"""
# 함수를 이용한 구현
def add(x, y):
    return x + y

val_x = 1
val_y = 2
val_sum = add(val_x, val_y)
print(val_sum)
print()

#------------------------------------
# 클래스를 이용한 구현
class Calc: # 클래스를 생성했고, 그 아래 여러 객체를 만들어 사용한다.
    name = 'Calc' # name이라는 변수에 Calc로 지정해서 정의한다.
    def __init__(self): # 언더바가 2개 붙어있는 함수들이 존재한다. 이는 해당 클래스를 이용해서 처음으로 객체가 만들어 질 때, 처음으로 만들어지는 함수를 뜻한다.
        self.value = 0 # value = 객체 변수 / 클래스 변수와는 다르게 각각의 인스턴스 안에서 개별 변수를 생성하는 것이다.
    
    def add(self, x, y): # 자기 자신을 인스턴스로 하나 받아오고, 뒤에 반환할 함수를 정의한다. 
        self.value = x + y
        return self.value
    
    def getLastValue(self):
        return self.value
    
myCalc = Calc()
print(type(myCalc))
yourCalc = Calc()
print()

print(myCalc.add(1, 2))
print(yourCalc.add(3, 4))
print()

print(myCalc.getLastValue())
print(yourCalc.getLastValue())
print()

print(myCalc.value)
print(yourCalc.value)
print()

print(Calc.getLastValue(myCalc))
print(Calc.getLastValue(yourCalc))
print()

print(Calc.name)
print(myCalc.name)
print(yourCalc.name)
print()

myCalc.name = 'MyCalc'
print(Calc.name)
print(myCalc.name)
print(yourCalc.name)
print()

Calc.name = 'Class - Calc'
print(Calc.name)
print(myCalc.name)
print(yourCalc.name)
print()
#---------------------------------------------------------------------------

"""
# 파이썬 객체지향 프로그래밍: 클래스 변수 (static변수) 의 사용 예
"""
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
print()
#---------------------------------------------------------------------------

"""
# 파이썬 객체지향 프로그래밍: 클래스 상속, 오버라이딩의 구현
"""
class Animal:
    def __init__(self):
        self._name = 'Animal'
        self.age = 0
#---------------------------------------------------------------------------