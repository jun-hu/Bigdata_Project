import sys
import urllib.request as req
import urllib.parse as parse
from bs4 import BeautifulSoup

API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
if len(sys.argv) <=1:
    print("add station number")
    sys.exit()
regionNumber = sys.argv[1]

values={
'stnId':regionNumber
}
params=parse.urlencode(values)
url=API+"?"+params
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

