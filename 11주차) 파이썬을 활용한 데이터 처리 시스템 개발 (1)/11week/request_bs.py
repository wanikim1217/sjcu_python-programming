# pip install requests

import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B0%9C%EB%B0%9C%EC%9E%90')
print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')

# Title 확인
title = soup.find('title')
print(title.get_text())

total_tit = soup.find_all( class_ = 'total_tit')
for one in total_tit:
	print(one.getText())