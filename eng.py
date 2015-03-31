import urllib2
import codecs
import re
from bs4 import BeautifulSoup

f = codecs.open('eng.txt','w','utf-8')

n=0
for j in range (1,5):
    req = urllib2.Request('http://158.108.40.231/?page_id=271&paged='+str(j))
    res = urllib2.urlopen(req)
    page = res.read()


    soup = BeautifulSoup(page)
    for k in range(0,5):
        mydiv = soup.find('div', { 'id' : 'postTabs_'+str(k)+'_271'})
        li = mydiv.find_all('li')
        link=[]
        title=[]
        for a in li:
            string = a.get_text()
            result = re.search('[0-9]*[0-9] [A-Z][a-z][a-z] [0-9][0-9]',string)
            #print date.group(0) + ", " + string
            date = result.group(0)

            '''
            result = re.search('[A-Z][a-z][a-z]',date)
            month = result.group(0)
            month = {"Jan":"1","Feb":"2","Mar":"3"}
            if month == "Jan":
            elif month == "Feb":
            elif month == "Mar":
            elif month == "Apr":
            elif month == "May":
            elif month == "Jun":
            elif month == "Jul":
            elif month == "Aug":
            elif month == "Sep":
            elif month == "":
            print result.group(0)'''

            link.append(a.a.get('href'))
            title.append(a.a.get('title'))
        a=0
        for i in title:
            #f.write(link[a]+','+i+'\n')
            n+=1
            f.write(i+'\n')
            #f.write(i+ ',' +link[a]+'\n')
            #print link[a]    
            a+=1
print n
f.close()
