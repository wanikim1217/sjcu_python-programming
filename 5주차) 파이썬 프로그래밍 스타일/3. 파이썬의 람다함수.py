#---------------------------------------------------------------------------
"""
# 람다 함수 (익명 함수)

람다함수는 코드의 간결함과 메모리 절약에 도움이 됩니다.
"""

#---------------------------------------------------------------------------
"""
# 일반적인 함수
"""
def add(a,b):
    return a + b
result = add(1,2)
print(result)

#---------------------------------------------------------------------------
"""
# 간단한 람다 함수
"""
add = lambda a, b: a+ b
result = add(1,3)
print(result)

result = (lambda a, b: a + b)(1,4)
print(result)

result = (lambda a, b: a + b)(a = 1, b = 4)
print(result)

result = (lambda a, b = 4: a + b)(1)
print(result)

#---------------------------------------------------------------------------
"""
# 람다 함수의 활용 예: 조건문
"""
print((lambda a, b: a if a % 2 == 0 else b)(1,3))

#---------------------------------------------------------------------------
"""
# 람다 함수의 활용 예: 문자열 포맷팅
"""
print((lambda a, b: '{} + {} = {}'.format(a, b, a + b))(1,5))

#---------------------------------------------------------------------------
"""
# 람다 함수의 활용 예: 리스트의 정렬
"""
data = ['Python Lambda', 'Python', 'Hello World']
data.sort(key = lambda x: len(x))
print(data)

#---------------------------------------------------------------------------
"""
# 람다 함수의 활용 예: 새로운 리스트 만들기
"""
data = list(map(lambda x: x * 2, range(10)))
print(data)

#---------------------------------------------------------------------------
"""
# 람다 함수의 활용 예: 필터링
"""
data = list(filter(lambda x: x % 2 == 0, range(10)))
print(data)

#---------------------------------------------------------------------------
"""
# 람다 함수의 활용 예: 함수의 반환
"""
def calc(op):
    if op == '+':
        return lambda a, b: a + b
    elif op == '-':
        return lambda a, b: a - b
    elif op == '*': 
        return lambda a, b: a * b
    elif op == '/':
        return lambda a, b: a / b
    else: 
        return lambda a, b: a % b
myCalc = calc('+')
print(myCalc(1,6))

#---------------------------------------------------------------------------
"""
# 재귀함수의 예: 팩토리얼
"""
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)
print(factorial(5))

factorial = lambda n: 1 if n == 1 else n * factorial(n-1)
print(factorial(5))

#---------------------------------------------------------------------------
"""
# 추가 Thread 활용
"""
# https://docs.python.org/ko/3/library/threading.html 
import threading
import time

def thread_main(x):
    print(f'{x} - Thread Start')
    time.sleep(1)
    print(f'{x} - Thread End')

print('----- Threads Start -----')
thread_main(0)
thread_main(1)
thread_main(2)
thread_main(3)
thread_main(4)
thread_main(5)
thread_main(6)
thread_main(7)
thread_main(8)
thread_main(9)
print('----- Threads End -----')

print('----- Multi Threads Start -----') 
threads = []
for i in range(10):
    t = threading.Thread(target=thread_main, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print('----- Multi Threads End -----') 

#---------------------------------------------------------------------------
"""
# 추가 Thread 활용 - 임계 구역
"""
number = 0
lock = threading.Lock()

def thread_counter(x):
    global number
    print(f'{x} - Thread Start - {number}')
    lock.acquire() # 멀티를 하더라고 이 아래부터는 동시에 접근하지 못하고 배터적으로 실행하도록 만드는 함수
    time.sleep(1)
    number += 1
    print(f'{x} - Thread End - {number}')
    lock.release() # lock을 푼다는 의미의 함수
 
print('----- Threads Start -----')
thread_counter(0) 
thread_counter(1)
thread_counter(2)
thread_counter(3)
thread_counter(4)
thread_counter(5)
thread_counter(6)
thread_counter(7)
thread_counter(8)
thread_counter(9)
print('----- Threads End -----') 

print('----- Multi Threads Start -----') 
number = 0
threads = []
for i in range(10):
    t = threading.Thread(target=thread_counter, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print('----- Multi Threads End -----')
