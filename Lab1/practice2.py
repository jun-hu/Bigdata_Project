import urllib.request
from bs4 import BeautifulSoup
import gzip

url = "http://info.finance.naver.com/marketindex/"
res=urllib.request.urlopen(url)
data=res.read()
#html=gzip.decompress(data).decode("ko")

text=data.decode("euc-kr")
#print(text)
soup=BeautifulSoup(text,'html.parser')


#price=soup.select_one("#header > div.snb_area > div > div.sta > form > fieldset > legend")
price=soup.select_one("li.on > a.head.usd > div > span.value")
print(price)


