import urllib2
import codecs
from bs4 import BeautifulSoup

f = codecs.open('topic_intaff.txt','w','utf-8')

req = urllib2.Request('http://www.intaff.ku.ac.th/Admin/WBfund/list_funds.php')
res = urllib2.urlopen(req)    
page = res.read()
soup = BeautifulSoup(page,'html.parser')
table = soup.find_all('table')
rows = []
news = []
links = []
num = 0

for i in table:
    row = i.tr.td.a
    if row != None and row not in rows:
        rows.append(row)
        
for i in rows:
    num+=1
    new = i.get_text()
    news.append(new) 
    links.append(i.get('href'))   
    link = "http://www.intaff.ku.ac.th/Admin/WBfund" + i.get('href')
    #print "http://www.intaff.ku.ac.th/Admin/WBfund" + i.get('href')
    #f.write(new+","+link+"\n")
    f.write(new+"\n")
    print link


print num
f.close()
