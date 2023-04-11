#---------------------------------------------------------------------------
"""
# Dictionary 자료구조의 특징과 기본적인 사용법
"""
var = {'name': 'Chris', 'age': 23, 1: ['a', 'b', 'c']}
print(var)
print(var['name'])

var['age'] = 33
print(var)

#------------------------------------
# del연산자: 1이라는 key를 가지고 있는 item을 삭제하라 
del var[1]
print(var)
var[1] = 'Hi'
print(var)

#------------------------------------
# update: 여러개의 key에 대한 value를 한 번에 업데이트해라 
var.update({'name' : 'Hans', 'age' : 30})
print(var)

#------------------------------------
# 두 개의 딕셔너리 병합
data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = {'3rd' : 'hans', '4th' : 'james', '5th' : 'jenny'}
var = {**data_1, **data_2} # **를 통해 두개의 딕셔너리를 합쳐서 하나의 딕셔너리로 통합한다.
print(var)
var = data_1 | data_2   # Python 3.9 이상에서만 사용 가능
print(var)

#---------------------------------------------------------------------------
"""
# 얕은 복사와 깊은 복사
"""
data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1 # 얕은 복사
print(data_1)
print(data_2)
data_1['1st'] = 'hans'
print(data_1)
print(data_2)

data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1.copy() # 깊은 복사 = 실제 복제
print(data_1)
print(data_2)
data_1['1st'] = 'hans'
print(data_1)
print(data_2)

#---------------------------------------------------------------------------
"""
# Dictionary Comprehension의 특징과 예
"""
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var)
var = { name : age for name, age in var.items() if age < 20}
print(var)

#---------------------------------------------------------------------------
"""
# Dictionary 관련 함수 
"""
#------------------------------------
# keys() : Dictionary의 key를 반환
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var.keys())

#------------------------------------
# values() : Dictionary의 value를 반환
print(var.values())

#------------------------------------
# items() : Dictionary의 key와 value를 반환 
print(var.items())

#------------------------------------
# clear() : Dictionary의 모든 값을 제거
var.clear()
print(var)

#------------------------------------
# get() : Dictionary의 특정 key의 value를 반환
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print('chris' in var)
print(var.get('chris'))
print('hans' in var)
print(var.get('hans')) # None
print(var.get('hans', 'hans is not in var')) # Hans의 정보가 없다면 뒤의 문구를 출력하게도 할 수 있다.

#---------------------------------------------------------------------------
"""
# Dictionary 활용
"""
#------------------------------------
# 다양한 루프(Loop) 테크닉
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
for k, v in var.items():
    print(k, v)

for i, v in enumerate(['chirs', 'tommy', 'harry']):
    print(i, v)
    
name = ['chris', 'tommy', 'harry']
age = [10, 30, 20]
for k, v in zip(name, age):
    print(k, v)

#------------------------------------
# Json과 Dictionary 변환
import json

var = '{"chris" : 10, "tommy" : 30, "harry" : 20}'
print(var)
print(type(var))

# 문자열을 Dictionary로 변환
var = json.loads(var)
print(var)
print(type(var))

# Dictionary를 문자열로 변환
var = json.dumps(var)
print(var)
print(type(var))