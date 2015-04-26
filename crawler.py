# -*- coding: utf-8 -*- 
import urllib2
import codecs
import re
from bs4 import BeautifulSoup
import time
from datetime import date

def setGlobal():
    global listUrl
    global today
    global lastNid

def currentDate():
	today = date.today()
	return today

def Nid(mode):
	# r= read, w=write
	f = codecs.open('Nid.txt',mode,'utf-8')
	if mode == 'r':
		i = f.readline()
		i = i.strip('\n')
		lastNid = int(i)
	elif mode == 'w':
		f.write(str(lastNid+1))

def getHTML(url):
	#req = urllib2.Request("http://nisit.kasetsart.org/WebForm_Project_Detail.aspx?proj_code=157010010249")
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    page = res.read()
    HTML = BeautifulSoup(page,'html.parser')
    return HTML

def engAnnounce():
	# declare variables 
	f = codecs.open(str(today) +' engAnnounce.txt','w','utf-8')
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
	for i in range(1,numpage):
		HTML = getHTML(listUrl[0]+str(i))
		# each j for each categories in page_id=271
		for k in range(0,5):
			mydiv = HTML.find('div', { 'id' : 'postTabs_'+str(k)+'_271'})
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
					f.write(title +","+ link +","+ datePublish + "\n")
					print details
	print count  
	print len(totalLink)   
	f.close()

#NOT WORK
def engFund():
	# declare variables 
	f = codecs.open(str(today) +' engFund.txt','w','utf-8')
	numpage = 4    #number of total page 
	count = 0       #amount of news topics
	datePublish = ""
	totalLink = []
	details = ""
	link = ""
	title = ""
	month = {"Jan":"01", "Feb":"02", "Mar":"03", 
        "Apr":"04", "May":"05", "Jun":"06", 
        "Jul":"07", "Aug":"08", "Sep":"09", 
        "Oct":"10", "Nov":"11", "Dec":"12"}
	# get source code for each page
	for i in range(1,numpage):
		HTML = getHTML(listUrl[1]+str(i))
		print HTML
		for k in range(0,3):
			mydiv = HTML.find('div', { 'id' : 'postTabs_1_269'})
			print mydiv
    		li = mydiv.find_all('li')
    
    		# get details of each topics 
    		for a in li:
        		count += 1
        		string = a.get_text()
        		result = re.search('[0-9]*[0-9] [A-Z][a-z][a-z] [0-9][0-9]',string)

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
            		f.write(title +","+ link +","+ datePublish + "\n")
            		print details
	print count  
	print len(totalLink)   
	f.close()

def nisit():
	#declare variables
	d=codecs.open("nisit",'a','utf-8')
	topic=codecs.open(str(today) + ' nisit.txt','w','utf-8')
	pattern = "http://nisit.kasetsart.org/"
	data = []
	totalLink = []
	num=0
	HTML = getHTML(listUrl[2])
	#http://nisit.kasetsart.org/WebForm_Project_Detail.aspx?proj_code=156010010473
	table = HTML.find('table')

	rows = table.find_all('tr')
	for line in rows:
		i = line.find_all('td')
		n=0
		for j in i :
			n+=1
			link = j.a
			if n==2 and link != None:
				num+=1
				#print num
				title = j.get_text()
				patternLink = pattern + link.get('href')
				if patternLink not in totalLink:
					totalLink.append(patternLink)
					result = re.search('code=[0-9]+',patternLink)
					codestring = result.group(0)
					code = codestring.split('=')
					details = title + "," + patternLink +","+ nisitDetails(code[1])
					print details
					data.append(details)
					topic.write(details+"\n")
					#print link.get('href')
					#f.write("http://nisit.kasetsart.org/"+link.get('href')+"\n")
					#print details
	print num
	print len(totalLink)
	topic.close()

def nisitDetails(code):
	#declare variables
	datePublish = ""
	dateStart = ""
	url = ("http://nisit.kasetsart.org/WebForm_Project_Detail.aspx?proj_code=")
	HTML = getHTML(url + code)
	
	level = HTML.find('span', { 'id' : 'LabelPROJ2_LEVEL'})
	types = level.get_text()

	#3/3/2558 16:22:27
	#2015-04-09 yyyy-mm-dd
	findDatetime = HTML.find('span', { 'id' : 'LabelProj_DateCreate'})
	datetime = findDatetime.get_text()
	result = re.search('[0-9]*[0-9]/[0-9]*[0-9]/[2][5][5][0-9]',datetime)
	date = result.group(0)
	splitdate = date.split('/')
	datePublish = str(int(splitdate[2]) - 543)
	if len(splitdate[1]) == 1:
		datePublish = datePublish + "-0" + splitdate[1]
	else:
		datePublish = datePublish + "-" +splitdate[1]
	if len(splitdate[0]) == 1: 
		datePublish = datePublish + "-0" + splitdate[0]
	else:
		datePublish = datePublish + "-" +splitdate[0]

	findDatetime = HTML.find('span', { 'id' : 'LabelProj_DateManage'})
	datetime = findDatetime.get_text()
	result = re.search('[0-9]*[0-9]/[0-9]*[0-9]/[2][5][5][0-9]',datetime)
	date = result.group(0)
	splitdate = date.split('/')
	dateStart = str(int(splitdate[2]) - 543)
	if len(splitdate[1]) == 1:
		dateStart = dateStart + "-0" + splitdate[1]
	else:
		dateStart = dateStart + "-" +splitdate[1]
	if len(splitdate[0]) == 1: 
		dateStart = dateStart + "-0" + splitdate[0]
	else:
		dateStart = dateStart + "-" +splitdate[0]
	
	details = types + "," + datePublish + "," + dateStart
	#print details
	return details

def intaff():
	#declare variables
	f=codecs.open(str(today) +' intaff.txt','w','utf-8')
	totalLink = []
	datePublish = ""
	date = ""
	numpage = 7
	month = {"มกราคม":"01", "กุมภาพันธ์":"02", "มีนาคม":"03", 
		"เมษายน":"04", "พฤษภาคม":"05", "มิถุนายน":"06", 
		"กรกฎาคม":"07", "สิงหาคม":"08", "กันยายน":"09", 
		"ตุลาคม":"10", "พฤศจิกายน":"11", "ธันวาคม":"12"}
	for i in range(0,numpage):
		HTML = getHTML(listUrl[3]+str(i))
		data = HTML.find_all('header', { 'class' : 'loop-data'})
		for j in data:
			loopTitle = j.find('h3',{'class':'loop-title'})
			title = loopTitle.get_text()
			link = loopTitle.a.get('href')
			if link not in totalLink:
				totalLink.append(link)
				#เมษายน 16, 2015
				#2015-04-09 yyyy-mm-dd
				findDatetime = j.find('p',{'class':'meta'})
				datetime = findDatetime.get_text()
				splitdate = datetime.split(' ')
				s = splitdate[0].encode('utf-8')
				if len(splitdate[1]) == 2:
					date = "0" + splitdate[1]
				else:
					date = splitdate[1]
				datePublish = splitdate[2] +"-"+ month[s] +"-"+ date[:2]
				details = title +","+ link +","+ datePublish
				print details
				f.write(details + "\n")
	print len(totalLink)
	f.close()

def ku():
	'''
	# get date if news not exist in database
	d = codecs.open('ku.txt','w','utf-8')
	d.write(str(today)+"\n")
	d.close()
	'''

	#declare variables
	#Nid,Title,Link,Content,Pic,DatePubish,DateStart
	f = codecs.open(str(today) +' ku.txt','w','utf-8')
	totalLink = []
	datePublish = ""
	date = ""
	data = []
	'''
	HTML = getHTML("http://www.ku.ac.th/web2012/index.php?c=adms&m=mainpage1")
	items = HTML.find_all('div',{'class':'dataitem'})
	for i in items:
		link = i.a
		link = link.get('href')
		linkRemove = re.sub(remove,'',link)
		img = i.find('img')
		img = img.get('src')
		text = i.find('div',{'class':'title'})
		title = text.get_text()
		text = i.find('div',{'class':'comment'})
		title = title + text.get_text()
		#print title
	'''
	for i in range(4,9):
		HTML = getHTML(listUrl[i])
		table = HTML.find('table')
		row = table.find_all('a')
		for j in range(0,len(row)+1):
			if j==len(row)-1:
				break
			if j%2==0:
				title = row[j].get_text().strip()+" "+row[j+1].get_text()
				title = title.strip()
				link = row[j].get('href')
				datePublish = link[62:66] +"-"+ link[66:68] +"-"+ link[68:70] #format yyyymmdd
				details = title + "," + link +","+ datePublish
				data.append(details)
				print str(j) + ":"+ details
				f.write(title + "," + link +","+ datePublish+"\n")
		print len(data)
	


listUrl = ["http://158.108.40.231/?page_id=271&paged=","http://www.eng.ku.ac.th/?page_id=269&paged=",
		"http://nisit.kasetsart.org/WebForm_Index_Search_Result_1year.aspx?day=back&campus=1",
		"http://iad.intaff.ku.ac.th/wordpress/?cat=25&paged=",
		"http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%C1%CB%D2%C7%D4%B7%C2%D2%C5%D1%C2&load=tab&lang=thai&ip=10&id=87",
		"http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%B9%D4%CA%D4%B5&load=tab&lang=thai&ip=10&id=88",
		"http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%BB%C3%D0%AA%D8%C1/%CA%D1%C1%C1%B9%D2/%CD%BA%C3%C1&load=tab&lang=thai&ip=10&id=89",
		"http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%A1%D2%C3%C8%D6%A1%C9%D2&load=tab&lang=thai&ip=10&id=126",
		"http://www.ku.ac.th/web2012/index.php?c=adms&m=viewallnews&page=%A2%E8%D2%C7%CA%D2%C3%E1%C5%D0%A1%D4%A8%A1%C3%C3%C1&page1=%A2%E8%D2%C7%A1%D2%C3%C3%D1%BA%C3%D2%A7%C7%D1%C5&load=tab&lang=thai&ip=10&id=128",
		"http://grad.ku.ac.th/index2.php",
		"http://training.ku.ac.th/2015/"]
listFile = ["engAnnounce.txt","engFund.txt","nisit.txt","intaff.txt","ku.txt","grad.txt","training.txt"] 
today = currentDate()
Nid('r')
setGlobal()
ku()