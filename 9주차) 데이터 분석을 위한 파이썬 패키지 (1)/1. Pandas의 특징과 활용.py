#---------------------------------------------------------------------------
"""
# pip install pandas
"""
import pandas as pd

#---------------------------------------------------------------------------
"""
# 리스트 / 딕셔터리-> 시리즈(Series)
"""
series = pd.Series([100, 90, 80], index=['KOR', 'MATH', 'ENG'])
#series = pd.Series({'KOR':100, 'MATH':90, 'ENG':80})
series.name = '점수'
series.index.name = '과목'

print(series)
print()

print('index : {}'.format(series.index))
print('values : {}'.format(series.values))
print()

#---------------------------------------------------------------------------
"""
# 딕셔너리 -> 데이터프레임(DataFrame)
"""
data = {'Subject':['KOR', 'MATH', 'ENG'], 'Score':[100, 90, 80]}
dataFrame = pd.DataFrame(data)

print(dataFrame)
print('index: {}'.format(dataFrame.index))
print('values: {}'.format(dataFrame.columns))
print('vales: {}'.format(dataFrame.values))
print()
print('dataFrame[\'Subject\]: {}'.format(dataFrame['Subject']))
print('dataFrame[\'Score\]: {}'.format(dataFrame['Score']))
print()

print('dataFrame[0:2] : {}'.format(dataFrame[0:2]))
print('dataFrame.iloc[:2] : {}'.format(dataFrame.iloc[:2])) # iloc = index location의 약자/ index 값을 기준으로 범위를 추출
print('dataFrame.loc[:2] : {}'.format(dataFrame.loc[:2])) # loc = 조건식까지 포함하여, 조금 더 유연하고 다양하게 데이터를 가져올 수 있다.
# -> iloc와 loc의 차이: loc의 경우 0,1,2까지 모두 추출한다는것을 알 수 있다. 헷갈리지 않는 것이 중요하다.
print()

print('dataFreme[\'Subject\'][0] : {}'.format(dataFrame['Subject'][0]))
print()

print(dataFrame[dataFrame['Score'] >= 90])
print(dataFrame.loc[dataFrame['Score'] >= 90, ['Subject']])
print()

print(dataFrame.describe())
print()

dataFrame['Score'] = 100
print(dataFrame)
print()

dataFrame['Score'] = [100, 90, 80]
dataFrame['Grade'] = ['A+', 'A', 'B']
print(dataFrame)
print(dataFrame[['Subject','Grade']])
print()

del dataFrame['Score']
print(dataFrame)
print()

dataFrame.drop(['Grade'], axis=1) # drop은 실제 데이터를 없앤 새로운 데이터 셋을 반환하는 것이다. 
print(dataFrame)
print()

dataFrame.drop(['Grade'], axis=1, inplace=True)
print(dataFrame)
print()

dataFrame.drop(dataFrame[dataFrame['Subject'] == 'KOR'].index, inplace=True)
print(dataFrame)
print()

#---------------------------------------------------------------------------
"""
# 엑셀(cvs) 파일 사용하기
"""
dataFrame = pd.read_csv('grade.csv')

print(dataFrame.head())
print(dataFrame.tail())
print()

print(dataFrame)
print(dataFrame.describe())
print()

'''
result = pd.crosstab(index = dataFrame.GRADE, columns = "count", margins = True)
print(result)

dataFrame = dataFrame[dataFrame['GRADE'] == 'A']
print(dataFrame)
'''
# 위의 문제 grade.csv에서 GRADE를 읽어오지 못하는 상황

dataFrame['MEAN'] = (dataFrame['KOR'] + dataFrame['MATH']) / 2
print(dataFrame)
print()

'''
dataFrame.drop(['GRADE'], axis=1, inplace=True)
dataFrame.to_csv('gradeA.csv', index=False)
'''
# 위의 문제 grade.csv에서 GRADE를 읽어오지 못하는 상황