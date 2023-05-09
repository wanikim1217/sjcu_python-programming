# pip install numpy
import numpy as np

#######################################33
# 기본 사용법
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

print(array[0][0])

subarray = array[ :, :2]
print(subarray)
print(subarray.shape)

array = np.arange(0, 10, 2)
print(array)

array = np.zeros((3,3))
print(array)

array = np.ones((3,3))
print(array)

array = np.eye(3)
print(array)

array = np.random.randint(0, 100, (3,3))
print(array)

array = np.full((8,8), 255)
print(array)

array = array.flatten()
print(array)

array = array.reshape((8,8))
print(array)

array[2:6, 2:6] = 0
print(array)

array = np.where(array == 0, 1, array)
print(array)

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

result = np.dot(arrayA, arrayB)
print(result)




