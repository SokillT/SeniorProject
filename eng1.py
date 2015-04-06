import urllib2
import codecs
import re
from bs4 import BeautifulSoup

f = codecs.open('eng1.txt','w','utf-8')

# declare variables 
numpage = 53	#number of total page 
count = 0		#amount of news topics
datePublish = ""
totalLink = []
details = ""
link = ""
title = ""
month = {"Jan":"01", "Feb":"02", "Mar":"03", 
		"Apr":"04", "May":"05", "Jun":"06", 
		"Jul":"07", "Aug":"08", "Sep":"09", 
		"Oct":"10", "Nov":"11", "Dec":"12"}
url = ["http://158.108.40.231/?page_id=269&paged=","http://158.108.40.231/?page_id=271&paged="]	#[0]for fund, [1]forannoucement

# get source code for each page
for i in range(1,numpage):
	req = urllib2.Request("http://158.108.40.231/?page_id=271&paged="+str(i))
	res = urllib2.urlopen(req)
	page = res.read()
	soup = BeautifulSoup(page)

	# each j for each categories in page_id=271
	for k in range(0,5):
		mydiv = soup.find('div', { 'id' : 'postTabs_'+str(k)+'_271'})
		li = mydiv.find_all('li')

		# get details of each topics 
		for a in li:
			count += 1
			string = a.get_text()
			result = re.search('[0-9]*[0-9] [A-Z][a-z][a-z] [0-9][0-9]',string)
            #print date.group(0) + ", " + string
            #2015-04-09 yyyy-mm-dd
			date = result.group(0)
			splitdate = date.split(' ')
			if len(splitdate[0]) == 1:
				d = "0" + splitdate[0]
			else:
				d = splitdate[0]
			datePublish = "20"+splitdate[2]+"-"+month[splitdate[1]]+"-"+d
			link = a.a.get('href')
			title = a.a.get('title')
			if link not in totalLink:
				totalLink.append(link)
				details = title +","+ link +","+ datePublish
				f.write(details + "\n")
				print details
print count  
print len(totalLink)   
f.close()
