#---------------------------------------------------------------------------
"""
# if 문의 활용 예
"""

# 기본
cond = True
if cond:
    print("Execute")
    
#------------------------------------
# if ~ else
var = 10
if 0 < var:
    print("Big")
else:
    print("Small")

#------------------------------------  
# if ~ elif ~ else
var = input("Entre a number: ")
var = int(var)

if 10 < var:
    print("Bigger than 10")
elif 5 < var:
    print("Bigger than 5")
elif 0 < var: 
    print("Bigger than 0")
else:
    print("Too Small")

#------------------------------------
# 비교 / 논리 연산자
x, y = 10, 20
if 0 < x and y < 30:
    print("Good")
else:
    print("Bad")

var = input("Enter a number: ")
var = int(var)
if x != var and y != var:
    print("Bad")
else:
    print("Good")

#------------------------------------
# in, not 연산자

var = [1, 2, 3]
print (1 in var)

var = ["chris", "tommy", "harray"]
print("chris" in var)

var = "Hello Python"
print("J" not in var)

#------------------------------------
# 조건부 표현식
var = input("Enter a number: ") 
var = int(var)

var = "Big" if 10 < var else "Small"
print(var)

#---------------------------------------------------------------------------
"""
# while 문의 활용 예
"""

cond = 0
while cond < 10:
    cond = cond + 1
    if cond % 3 == 0:
        continue
    if cond % 5 == 0:
        break
    print(cond)

while True:
    var = input("Enter a number: ")
    var = int(var)
    if var == 0:
        print("Good Bye!")
        break

#---------------------------------------------------------------------------
"""
# for 문의 활용 예
"""
var = [1, 2, 3]
for one in var:
    print(one)
    
var = [(1,1), (2,2), (3,3)] # 리스트인데 그 안에 튜플이 존재, 따라서 리스트에서 인자를 가져오면 튜플이 가져오게 된다.
for (first, second) in var: # 튜플로 받아올 수 있음을 보여준다.
    print(first, second)
    
sum = 0
var = range(1,11)
for one in var:
    if (one % 2 == 0):
        continue
    sum = sum + one
print(sum)

