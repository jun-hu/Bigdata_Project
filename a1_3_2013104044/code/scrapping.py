from bs4 import BeautifulSoup

html="""
<html><body>
<div id="project">
<h1 id="title">B</h1>
<p id ='body'>D</p>
<p>DA</p>

<ul class='items'>
<li>C</li>
<li>S</li>
<li>H</li></ul>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')

p1=soup.html.body.p
p2=p1.next_sibling.next_sibling

print(p1.string)
print(p2.string)

h1=soup.select_one("div#project > h1").string
print("h1 =",h1)

li_list=soup.select("div#project > ul.items > li")
for li in li_list:
    print("li =",li.string)
