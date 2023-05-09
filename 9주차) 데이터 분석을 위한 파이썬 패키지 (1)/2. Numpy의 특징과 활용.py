#---------------------------------------------------------------------------
"""
# pip install numpy
"""
import numpy as np

#---------------------------------------------------------------------------
"""
# 기본 사용법
"""
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

array = np.array(data) 
print(array)
print(array.dtype)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.nbytes)
print()

print(array[0][0]) # data의 슬라이싱

subarray = array[ :, :2] # array안에서 구간을 정해서 데이터를 추출가능하다. / : -> 모든 행 / :2 -> 0,1열만 출력
print(subarray)
print(subarray.shape)
print()

#------------------------------------
array = np.arange(0, 10, 2)
print(array)
print()

array = np.zeros((3,3))
print(array)
print()

array = np.ones((3,3))
print(array)
print()

array = np.eye(3) # 단위 행렬이 만들어진다
print(array)
print()

array = np.random.randint(0, 100, (3,3))
print(array)
print()

#------------------------------------
array = np.full((8,8), 255)
print(array)
print()

array = array.flatten() # 8x8이 아니라 하나로 쭉 펴서 출력
print(array)
print()

array = array.reshape((8,8)) # 다시 8x8로 모양을 만들어서 출력 / 행과 열의 구조 변경
print(array)
print()

#------------------------------------
array[2:6, 2:6] = 0
print(array)
print()

array = np.where(array == 0, 1, array) # np.where 
print(array)
print()

#------------------------------------
arrayA = np.array([1,2,3])
arrayB = np.array([4,5,6])
array = np.concatenate((arrayA, arrayB))
print(array)

array = arrayA + arrayB
print(array)

array = arrayA * arrayB
print(array)

array = arrayA / arrayB
print(array)

result = np.dot(arrayA, arrayB) # np.dot = 행렬 곱
print(result)