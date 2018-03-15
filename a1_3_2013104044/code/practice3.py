import urllib.request as req
from bs4 import BeautifulSoup 
import re

html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""
soup=BeautifulSoup(html,"html.parser")

htlist=soup.find_all('a',attrs={'href':re.compile(r"^https://")})
#soup.find_all("a",class_"sister")
#soup.find_all(class_=re.compile("itl"))
#def has_six_characters(css_class)
#    return css_class is not None and len(css_class) ==6
#soup.find_all(class_=has_six_characters)
#soup.find_all("a",attrs{"class":"sister"})

for e in htlist:
    print(e.get('href'))
   # http= e.find('a',attrs={'href':re.compile(r"^https://")})
   # print(http)
    
