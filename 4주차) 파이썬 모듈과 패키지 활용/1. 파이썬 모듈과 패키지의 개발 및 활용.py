#---------------------------------------------------------------------------
"""
# import 함수 사용의 예
"""
import calc
from calc import sum

print(calc.sum(1, 2))
print(sum(1, 2))

#---------------------------------------------------------------------------
"""
# PYTHONPATH 환경변수 설정 고려
"""
import calculate.say.hello # 패키지를 import를 했는데도, Hello, Package가 출력된 이유는 hello.py안에는 함수가 있는 것이 아닌 문자열 출력 기능하나만을 가지고 있기 때문이다.

import calculate.say.talk as talk # calculate안의 say.py안의 talk함수를 talk라는 단어로 불러서 가지고 오겠다는 의미
talk.talk("Hello World")

from calculate.calc.multi import multi # calculate안의 calc.py안의 multi함수를 multi라는 단어로 불러서 가지고 오겠다는 의미
print(multi(3, 3))

from calculate.calc import * # *를 함으로써 calc안에 모든 파이썬 파일을 import해서 다 쓰겠다는 의미
print(multi.multi(2, 2))
print(sum.sum(1, 2))

