#---------------------------------------------------------------------------
"""
# pip install beautifulsoup4 / 구글 코렙에서 !를 붙이는 경우, 명령문으로 시작해라는 의미
"""
from bs4 import BeautifulSoup

#---------------------------------------------------------------------------
html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sisterv" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print('*' * 30)

print(soup.title)
print(soup.title.parent.name)
print('*' * 30)

print(soup.p)
print('*' * 30)

print(soup.a)
for link in soup.find_all('a'):
  print(link.get('href'))
#---------------------------------------------------------------------------