import urllib2
import codecs
from bs4 import BeautifulSoup

def getHTML(url):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    page = res.read()
    HTML = BeautifulSoup(page,'html.parser')
    return HTML

def eng(HTML):
    for k in range(0,5):
        mydiv = HTML.find('div', { 'id' : 'postTabs_'+str(k)+'_271'})
        li = mydiv.find_all('li')
        link=[]
        title=[]
        for a in li:
            link.append(a.a.get('href'))
            title.append(a.a.get('title'))
        a=0
        for i in title:
            n+=1
            a+=1
            print k 

def ku(HTML):
    f = codecs.open('ku.txt','w','utf-8')
    table = HTML.find('table')
    row = table.find_all('a')
    data = []

print row
#row.pop(0)
#print row[0]
#print row[1]
print len(row)

for i in range(0,len(row)+1):
    if i>=len(row):
        break
    if i%2==0:
        line = row[i].get_text()+" "+row[i+1].get_text()
        #print str(i)+line
        f.write(line +"\n")

f.close()


listUrl = codecs.open('listUrl.txt','r','utf-8')
for url in listUrl:
    page = getHTML(url)


