import urllib2
import codecs
import re
from bs4 import BeautifulSoup

f = codecs.open('topic_ku.txt','w','utf-8')

req = urllib2.Request('http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&time=20120714023131&load=tab&lang=thai&ip=10&id=87&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%C1%CB%D2%C7%D4%B7%C2%D2%C5%D1%C2')
res = urllib2.urlopen(req)    
page = res.read()

soup = BeautifulSoup(page)
table = soup.find('table')
row = table.find_all('a')
data = []


print len(row)

for i in range(0,len(row)+1):
    if i>=len(row):
        break
    if i%2==0:
        line = row[i].get_text()+" "+row[i+1].get_text()
        #print str(i)+line
        line = line.strip()
        link = row[i].get('href')
        date = link[62:70] #format yyyymmdd
        f.write(line+"\n")
    	#f.write(line +","+link+"\n")
    	print line.strip()
    	

f.close()
