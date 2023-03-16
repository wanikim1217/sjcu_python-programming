#---------------------------------------------------------------------------
"""
# 파이썬 함수 사용의 예
"""

# 파라미터도 없고 리턴값도 없음
def hello():
    print("Hello World")
    
hello()
    
#------------------------------------
# 파라미터와 리턴값이 있음
def add(x, y):
    print(x)
    print(y)
    return x + y

val_x = 1
val_y = 2
val_sum = add(val_x, val_y)
print(val_sum)

#------------------------------------
# 호출할 때 매개변수(인자)의 이름을 지정할 수 있음
print(add(y = val_y, x = val_x))

#------------------------------------
# 호출할 때 매개변수(인자)의 이름을 지정할 수 있음
def add(x, y = 10):
    print(x)
    print(y)
    return x + y

print(add(1,2))
print(add(1))

#------------------------------------
# 매개변수의 개수가 가변적인 함수
def sum(*values): # 파라미터(인자)의 개수를 모를 때 사용
    result = 0
    for one in values:
        result = result + one
    return result

result = sum(1, 2, 3)
print(result)

#------------------------------------
# 여러개의 값을 반환하는 함수
def calc(a, b): 
    return a + b, a - b

result = calc(1,3)
print(result)

x, y = calc(1,3) # 튜플로 반환하지 않고 , 각각의 변수에 반환받는 법
print(x)
print(y)

#------------------------------------
# 변수의 스코프(범위)
val = 0
def processing(data):
    global val # val이라는 변수는 함수 내에서만 정의되어 나만 사용하는 것이 아닌 밖에 있는 변수를 내가 사용하는 것이라는 것을 나타낸다
    val = data
    data = data * 10
    return data * data

data = 10
result = processing(data)
print(val)
print(data)
print(result)

#------------------------------------
# Call by Reference
def processing(data):
    data[0] = 100
    
val = [1, 2, 3]
processing(val)
print(val)