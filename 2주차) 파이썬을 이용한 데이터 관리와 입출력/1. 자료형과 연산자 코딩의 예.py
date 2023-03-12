"""
자료형과 연사자 코딩의 예
"""

#---------------------------------------------------------------------------
"""
# 정수, 실수, 16진수의 사용
"""
variable = 123
print(variable)

variable = 1.23E2
print(variable)

variable = 1.23e2
print(variable)

variable = 1.23e-2
print(variable)

variable = 0x1f
print(variable)

variable = 0x1F
print(variable)

#---------------------------------------------------------------------------
"""
# 숫자형 데이터를 위한 연산자의 사용
"""
variable = 3 / 4 # 나누기 연산자
print(variable)

variable = 2 ** 3 # 제곱 연산자
print(variable)

variable = 5 % 2 # 나머지 연산자
print(variable)

variable = 5 // 2 # 몫의 연산자
print(variable)

variable = 5 / 2 # 나누기 연산자
print(variable)

#---------------------------------------------------------------------------
"""
# 문자열 데이터의 표현 (이스케이프 코드)
"""
variable = """
Dongwan
"Hello World"
"""
print(variable)

variable = """Dongwan
'Hello World'"""
print(variable)

variable = """Dongwan\n\"Hello World\""""
print(variable)

#---------------------------------------------------------------------------
"""
# 문자열 데이터를 위한 기본 연산자
"""
variable = "Hello" + " " + "World"
print(variable)

variable = "Hello" * 2
print(variable)

variable = len("Hello World")
print(variable)
'''
print(variable[3])
오류코드: 
TypeError: 'int' object is not subscriptable 
len 함수를 사용함으로써 숫자 11인 정수로 인식함으로 int는 해독하지 못하는 상황이 발생한다.
'''

variable = "Hello World"
print(variable[3])
print(variable[-3])
print(variable[1:4])
print(variable[:5])
print(variable[6:])

#---------------------------------------------------------------------------
"""
# 문자열 데이터 포맷팅 (문자열 만들기)
"""
variable = "%d books" %3 # d = 정수 / %를 활용한 출력 방식
print(variable)

variable = "%s books" %"3" # s = 문자열 
print(variable)

variable = "%s books" %3 # s 문자열인데 뒤에 따옴표 없이 그냥 숫자를 입력해도 자동으로 문자열으로 인식하는 효과를 보인다.
print(variable)

variable = "I have {0} {1}.".format(3, "books") # .format() 출력 방식
print(variable)

number = 3
variable = f'I have {number + 2} books.' # f string 출력 방식
print(variable)

variable = "I have %d apples and %d books." %(number, number + 1)
print(variable)

variable = "The error rates : %d%%" %55 # %%를 두번 사용함으로써 % 기호를 입력한다.
print(variable)

#---------------------------------------------------------------------------
"""
# 문자열 데이터 포맷팅 (정렬 등 다양한 표현 방식)
"""
# 추가 이해가 필요한 부분

variable = "%10s" %"Hello" # 10이 들어간 이유: 우측 정렬 및 전체 문자열의 길이는 10.
print(variable)

variable = "%-10s" %"Hello" # -10이 들어간 이유: 좌측 정렬 및 전체 문자열의 길이는 10
print(variable)

variable = "{0:<10}".format("Hello") # 좌측 정렬 및 전체 문자열의 길이는 10
print(variable)

variable = "{0:>10}".format("Hello") # 우측 정렬 및 전체 문자열의 길이는 10
print(variable)

variable = "{0:^10}".format("Hello") # 가운데 정렬 및 전체 문자열의 길이는 10
print(variable)

variable = "{0:-^10}".format("Hello") # 가운데 정렬 및 전체 문자열의 길이는 10, 그리고 빈 공간에는 - 표시
print(variable)

variable = "%f" %3.141592 # f = 실수 / %를 활용한 출력 방식
print(variable)

variable = "%.4f" %3.141592 # 소수점 아래 4번째 까지 츨력
print(variable) 

variable = "%10.4f" %3.141592 # 전체 문자열의 길이는 10이고 소수점 아래 4번째 까지 츨력
print(variable) 

#---------------------------------------------------------------------------