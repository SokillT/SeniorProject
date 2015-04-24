import urllib2
import codecs
from bs4 import BeautifulSoup

#f = codecs.open('link2.txt','w','utf-8')

for j in range (1,6):
    req = urllib2.Request('http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&time=20120714023131&load=tab&lang=thai&ip=10&id=87&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%C1%CB%D2%C7%D4%B7%C2%D2%C5%D1%C2')
    res = urllib2.urlopen(req)
    page = res.read()

    print page
#f.close()
