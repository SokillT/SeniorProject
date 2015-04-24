from bs4 import BeautifulSoup
import codecs

f = codecs.open('link.txt','w','utf-8')

soup = BeautifulSoup(open('eng.html'))
mydiv = soup.find("div", { "class" : "postTabs_divs postTabs_curr_div" })
mydivs = soup.find('div',{'class':'postTabs_divs postTabs_curr_div'}).text
li = mydiv.find_all('li')
link=[]
title=[]
for a in li:
    link.append(a.a.get('href'))
    title.append(a.a.get('title'))
for i in title:
    a =0
    f.write(link[a]+','+i+'\n')
    a=a+1
    #print title[i]
print len(li)

f.close()

