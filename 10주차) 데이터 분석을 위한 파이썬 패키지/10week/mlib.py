# pip install matplotlib
# 설치한 라브러리 목록 확인 / 저장 : pip freeze > requirements.txt
# 라이브러리 설치 : pip install -r requirements.txt 

# https://matplotlib.org/
# https://www.w3schools.com/python/matplotlib_subplot.asp

import matplotlib.pyplot as plt
import numpy as np

# Scatter
x = np.random.randint(1, 100, size = 30)
y = np.random.randint(1, 100, size = 30)

plt.scatter(x, y)
plt.show()

# Plot
data = {'X data' : [1, 2, 3, 4, 5],'Y data' : [2, 4, 8, 10, 3]}

plt.plot('X data', 'Y data', data = data)
plt.show()

# Plot with Label
plt.plot('X data', 'Y data', data = data)
plt.xlabel('X Lable', labelpad=10)
plt.ylabel('Y Label', labelpad=10)
plt.show()

# Legend
plt.plot('X data', 'Y data', data = data, label = 'My Data')
plt.xlabel('X Lable', labelpad=10, fontdict={'color': 'red'}, loc='right')
plt.ylabel('Y Label', labelpad=10, fontdict={'color': 'blue'}, loc='top')
plt.legend()
plt.show()

# 2개의 데이터(꺽은 선)
plt.plot([1, 2, 3, 4], [2, 3, 7, 9], linestyle='dashed', marker='o', label='Up')
plt.plot([1, 2, 3, 4], [9, 6, 5, 2], linestyle='dotted', label='Down')
plt.xlabel('Up Data')
plt.ylabel('Down Data')
plt.grid(True)
plt.title('Up & Down')
plt.legend(loc='best', ncol=2, fontsize=10, frameon=True, shadow=True)

plt.show()

# 막대 그래프
x = np.arange(3)
years = ['2021', '2022', '2023']
values = [100, 200, 500]

plt.bar(x, values)
plt.xticks(x, years)
plt.show()

y = np.arange(3)
plt.barh(y, values)
plt.yticks(y, years)
plt.show()

# 파이 챠트
ratio = [10, 30, 40, 20]
labels = ['chris', 'tommy', 'harry', 'hans']
explode = [0, 0.10, 0, 0.10]

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode)
plt.show()

# 이미지로 저장
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode)
plt.savefig('pie.png')

# 객체지향 인터페이스 사용
x = np.arange(1, 5)     # [1, 2, 3, 4]

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(x, np.sqrt(x))     # left-top
ax[0][1].plot(x, -x)             # right-top
ax[1][0].plot(x, 2*x)            # left-bottom
ax[1][1].plot(x, 3*x)            # right-bottom

plt.show()
