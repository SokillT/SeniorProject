import urllib2
import codecs

from bs4 import BeautifulSoup

req = urllib2.Request('http://nisit.kasetsart.org/WebForm_Index_Search_Result_1year.aspx?day=next&campus=1')
res = urllib2.urlopen(req) 
page = res.read()
soup = BeautifulSoup(page,'html.parser')
f=codecs.open('nisit.txt','w','utf-8')
table = soup.find('table')
#print table

data = []
rows = table.find_all('tr')
for line in rows:
	i = line.find_all('td')
	each = []
	n=0
	for j in i :

		n+=1
		link = j.a
		if n == 2 and link != None:
			f.write(j.get_text() +",")
			each.append(j.get_text())
			each.append("http://nisit.kasetsart.org/"+link.get('href'))
			#print link.get('href')
			f.write("http://nisit.kasetsart.org/"+link.get('href')+"\n")
	
		data.append(each)


		
f.close()