################################################################
# 싱글톤 패턴

class Singleton(object):
    __instance = None
    
    def __new__(self):
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(self)
        return Singleton.__instance
        
    def __init__(self):
        if not Singleton.__instance:
            print('No instance')
        else:
            print('Instance : ', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

obj_1 = Singleton()
print(obj_1)
obj_2 = Singleton()
print(obj_2)

obj_1 = Singleton.get_instance()
print(obj_1)
obj_2 = Singleton.get_instance()
print(obj_2)

################################################################
# Stack 구현
class Stack():
    def __init__(self):
        self.stack = []
        
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

