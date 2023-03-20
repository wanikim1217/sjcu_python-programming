#---------------------------------------------------------------------------
"""
# 표준 라이브러리의 사용 (내장)
"""
# 표준 라이브러리는 import하여 사용한다.
# 대표적인 것만 살펴보며, 함께 메모해 드릴 인터넷 자료도 함께 참고하시면 좋겠습니다. 

#---------------------------------------------------------------------------
"""
# datetime
"""
import datetime
date = datetime.date(2023, 3, 1)
print(date)
print(date.isoweekday()) # 요일 표시

#---------------------------------------------------------------------------
"""
# time
"""
import time
current = time.time()
print(current)
current = time.localtime(current)
print(current)
current = time.strftime('%c', current) # 시간을 우리가 원하는 형식으로 변경해서 출력하는 함수/ 안에 들어가는 것은 다양하다
print(current)

#---------------------------------------------------------------------------
"""
# random
"""
import random
for count in range(5):
    print(f'count: {count}')
    print(random.randint(1, 10))
    time.sleep(1)
    
#---------------------------------------------------------------------------
"""
# 객체를 직접 저장하고 읽어 들이기

# 이해 조금 더 필요

"""

import pickle
data = {'chris': 1, 'tommy': 2, 'harry': 3}
file = open('pickle.txt', 'wb') # pickle.txt 파일을 하나 만들어서, wb = write binany 모드로 기록하겠다.
pickle.dump(data, file) # 조금전에 만든 파일에 dump, 기록을 하겠다.
file.close

file = open('pickle.txt', 'rb') # 조금전에 만든 pickle.txt 파일을 열어서, rb = read bite 모드로 열겠다.
data = pickle.load(file) # 조금전에 만든 파일을 load, 기록을 읽겠다.
file.close()
print(data)

#---------------------------------------------------------------------------
"""
# os

# 이해 조금 더 필요

"""
import os
print(os.environ['PATH'])
os.system('dir')
file = os.popen('dir')
print(file.read())
file.close()