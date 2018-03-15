import urllib.request
from bs4 import BeautifulSoup

url = "http://info.finance.naver.com/marketindex/"
res=urllib.request.urlopen(url)
data=res.read()

text=data.decode("euc-kr")
soup=BeautifulSoup(text,'html.parser')

#price=soup.select_one("#header > div.snb_area > div > div.sta > form > fieldset > legend")
price=soup.select_one("li.on > a.head.usd > div > span.value")
print(price.string)


