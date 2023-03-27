#---------------------------------------------------------------------------
"""
# try, except, else, finally 구문을 이용한 예외 처리
"""

#---------------------------------------------------------------------------
"""
# 존재하지 않는 파일을 읽기모드로 여는 경우: FileNotFoundError 후 종료
"""
# myFile = open('NotExist.txt', 'r')

#------------------------------------
"""
# 잘못된 접근: IndexError 후 종료
"""
# myList = [1, 2, 3]    
# print(myList[3])

#---------------------------------------------------------------------------
"""
# 예외처리: try ~ except
"""
try:
    myFile = open('NotExist.txt', 'r')
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)
#------------------------------------  
try:
    myList = [1, 2, 3]
    print(myList[3])
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.')
    print(e)
#------------------------------------
try:
    print('Hello world!')
    raise Exception('My Exception') # raise는 프로그램 개발자가 강제로 예외를 발생시킬 수 있는 것
except Exception as e:
    print(e)
    
#---------------------------------------------------------------------------
"""
# 예외처리: try ~ except ~ finally
"""
# 여러개의 예외를 한번에 처리하려면 튜플로 묶어서 처리할 수 있음
# except (FileNotFoundError, IndexError, ZeroDivisionError) as e:
try:
    myFile_1 = open('example.txt', 'w')
    myFile_1.write('Hello world!')
    myList = [1, 2, 3]
    result = myList[3] / 0 # 3번째 인덱싱후 0으로 나누기 -> 에러 발생 부분
    print(result)
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.')
    print(e)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
finally:
    myFile_1.close()
    print('항상 실행됩니다.')
    
#---------------------------------------------------------------------------
"""
# 예외처리: try ~ except ~ else
"""
try:
    myFile_2 = open('example.txt', 'r')
    data = myFile_2.readline()
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다.')
    print(e)
else:
    print(data)
    myFile_2.close()

#---------------------------------------------------------------------------
"""
# 예외처리: try ~ except ~ else ~ finally
"""
try:
    myList = [1, 2, 3]
    result = myList[3] / 0
except IndexError as e:
    print('리스트의 인덱스가 존재하지 않습니다.')
    print(e)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
    print(e)
else:
    print(result)
finally:
    print('항상 실행됩니다.')
    
#---------------------------------------------------------------------------
"""
# 예외 처리 vs. 조건문
"""
data = input('숫자를 입력하세요 : ')
try: 
    result = 10 * int(data)
    print(result)
except ValueError as e:
    print('숫자를 입력하세요.')
    print(e)

data = input('숫자를 입력하세요 : ')
if data.isdigit():
    result = 10 * int(data)
    print(result)
else:
    print('숫자를 입력하세요.')
    
#---------------------------------------------------------------------------
"""
# assert 조건식, '에러 메시지'
"""
data = input('7을 입력하세요: ')
try:
    assert data == '7', '7을 입력하세요'
except AssertionError as e:
    print(e)