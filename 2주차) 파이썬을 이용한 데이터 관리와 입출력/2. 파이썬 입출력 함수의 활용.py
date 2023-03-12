#---------------------------------------------------------------------------
"""
# 사용자가 input 함수를 통해 입력한 값은 문자열입니다. 
"""
variable = input()
print("Input String %s, Integer %d" %(variable, int(variable)))

#---------------------------------------------------------------------------
"""
# 사용자가 메시지를 표시하면서 입력받을 수 있습니다.
"""
variable = input("Enter a number: ")
variable = int(variable) ** 2
print(f'Result: {variable}')

#---------------------------------------------------------------------------
"""
# print를 이용한 다양한 출력 방법
"""
variable = [1,2,3,4,5]
print(f'List : {variable}')

variable = (1,2,3,4,5)
print(f'Tuple : {variable}')

print("Hello" "World")
print("Hello", "World") # ,를 입력하는 경우 띄워쓰기를 하는 것을 알 수 있다. 

for variable in range(1,10):
    print(variable, end=" ") # end=" " / end=""를 사용함으로 한 줄에 연달아 출력할 수 있다.
    
for variable in range(1,10):
    print(variable) # end=" "를 입력하지 않는 경우, 줄 바꿈이 나타나는 것을 알 수 있다.
    
#---------------------------------------------------------------------------
"""
# 새로운 파일에 데이터 쓰기
"""
file = open("test.txt", "w") # write 모드
for data in range(1,11):
    file.write(f'line{data} ')
file.close

#---------------------------------------------------------------------------
"""
# 기록한 데이터 읽기
"""
file = open("test.txt", "r") # read 모드
while True:
    line = file.readline() # readline = 한 줄씩 읽고자 한다.
    if not line:
        break
    print(line)
file.close
print()
print("기록 1")
print()

#---------------------------------------------------------------------------
"""
# 이미 존재하는 파일에 데이터 추가하기
"""
file = open("test.txt", "a") # append 모드
for data in range(1,11):
    file.write(f'\nline{data}\n')
file.close()

#---------------------------------------------------------------------------
"""
# 기록한 데이터 읽기 (전체 라인을 한번에 읽기)
"""
file = open("test.txt", "r")
lines = file.readlines() # readlines = 전체를 한 번에 읽어서 lines라는 변수에 저장한다.
for line in lines:
    print(line)
file.close()
print()
print("기록 2 (추가)")
print()

#---------------------------------------------------------------------------
"""
# 기록한 데이터 읽기 (read함수를 이용하여 전체를 한 번에 읽기)
"""
print('-' * 50)
file = open("test.txt", "r")
data = file.read()
print(data)
file.close()

#---------------------------------------------------------------------------
"""
# with ~ as 구문을 이용하여 간결한 코드 작성하기
"""
with open("test.txt", "r") as file:
    data = file.read()
    print(data)