#---------------------------------------------------------------------------
"""
# 리스트 자료구조의 특징과 기본적인 사용법
"""
var = [1,'chris',['tommy', 'harry'], ('hans', 2)]
print(var)
print(var[3])
print(var[3][0])
print(var[-1])

var[0]=7
print(var[: 2])

del var[2:]
print(var)

print(len(var))

#---------------------------------------------------------------------------
"""
# 리스트의 연산
"""
x = [1,2,3]
y = [4,5,6]
var = x + y
print(var)

var = x * 2
print(var)
#------------------------------------
# append() : 리스트의 마지막에 값을 추가
var = [1,2,3]
var.append(4)
print(var)

#------------------------------------
# extend() : 리스트의 마지막에 리스트를 추가
var.extend([10,11,12])
print(var)

#------------------------------------
# insert() : 리스트의 특정 위치에 값을 추가
var.insert(0, 0)
print(var)

#------------------------------------
# remove() : 리스트의 특정 값을 제거
var = var * 2
print(var)
var.remove(4) # 처음만 제거
print(var)

#------------------------------------
# pop() : 리스트의 특정 위치의 값을 제거
var.pop()
print(var)
var.pop(0)
print(var)

#------------------------------------
# count() : 리스트의 특정 값의 개수를 반환
print(var.count(2))

#------------------------------------
# index() : 리스트의 특정 값의 인덱스를 반환
print(var.index(3)) # 3의 값이 2번째 자리에 있음을 출력

try:
    print(var.index(5))
except ValueError:
    print('ValueError')

#------------------------------------
# sort() : 리스트의 값을 정렬
import random
var = list()
for i in range(10):
    var.append(random.randint(1, 100))
print(var)

var.sort()
print(var)

#------------------------------------
# reverse() : 리스트의 값을 역순으로 정렬
var.reverse()
print(var)

#------------------------------------
# clear() : 리스트의 모든 값을 제거
var.clear()
print(var)

#---------------------------------------------------------------------------
"""
# 리스트 컴프리헨션의 특징과 예
"""
var = []
# var = list()
for data in range(1,11):
    if data % 2 == 0:
        var.append(data)
print(var)

var = list(filter(lambda x: x % 2 == 0, range(11))) # filter = 내가 원하는 값만 필터링해서 가져오겠다는 의미
print(var)

var = [data for data in range(1,11) if data % 2 == 0]
print(var)

var = [(x,y) for x in range(1,11) for y in range(1,11) if x + y == 10]
print(var)

var = [x for x in range(1,11) if x % 2 == 0 if 5 < x] # if문은 2개이상도 지정할 수 있다.
print(var)

#---------------------------------------------------------------------------
"""
# 리스트 제너레이터의 특징과 예
"""
var = (data +10 for data in range(1,11) if data % 2 == 0)
print(var)

try: 
    print(next(var))
    print(next(var))    
    print(next(var))    
    print(next(var))    
    print(next(var))    
    print(next(var))    
except StopIteration:
    print('StopIteration')
    
#---------------------------------------------------------------------------
"""
# 리스트의 활용 _ 스택
"""
stack = [1, 2, 3]
stack.append(4)
stack.append(5)
print(stack)

var = stack.pop()
print(var)
print(stack)

var = stack.pop()
print(var)
print(stack)

# 참고
from collections import deque
queue = deque(["chris", "tommy", "harry"])
queue.append("hans")
print(queue)
     
var = queue.popleft()               
print(var)
print(queue) 

var = queue.popleft()         
print(var)
print(queue) 
