import sys
import urllib.request as req
import urllib.parse as parse
from bs4 import BeautifulSoup

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184"
#
res=req.urlopen(url)
data=res.read()

text=data.decode("utf-8")
print(text)
soup=BeautifulSoup(text,'html.parser')

#print(text)

title=soup.title
wf=soup.wf

#print(title.string)
print("#title=" + title.string)
print("#wf=" + wf.string)

