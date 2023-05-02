#---------------------------------------------------------------------------
"""
# 싱글톤 패턴 
= 오로지 하나의 객체만 만들 수 있게 강제해보겠다는 의미
"""

class Singleton(object): # object = 모든 클래스들의 베이스 클래스다
    __instance = None # 변수 설정, 아무것도 값이 없는 변수
    
    def __new__(self): # __new__ = 특별한 클래스 함수인데, 객체를 만들 떄 사용한다.
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(self)
        return Singleton.__instance
    
    def __init__(self): # __init__ = 객체를 만들 때 처음으로 호출되는 함수를 의미한다.
        if not Singleton.__instance:
            print('No instance')
        else:
            print('Instance: ', self.get_instance())
    
    @classmethod # 내가 아래에 정의한 함수는 특별한 의미의 특별한 함수이다. (클래스가 직접 호출할 수 있는 클래스 메소드(함수)이다.)
    def get_instance(cls): # 
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    
obj_1 = Singleton()
print(obj_1)
obj_2 = Singleton()
print(obj_2)
print()

obj_1 = Singleton.get_instance()
print(obj_1)
obj_2 = Singleton.get_instance()
print(obj_2)
print()

#---------------------------------------------------------------------------
"""
# Stack 구현
"""
class Stack():
    def __init__(self):
        self.stack = [] # 비어있는 리스트 제작
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = None 
        if self.isEmpty():
            print('Empty')
        else:
            data = self.stack.pop()
        return data
    
    def isEmpty(self):
        return len(self.stack) == 0
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())