# -*- coding: utf-8 -*- 
import codecs

#INSERT INTO `news_news`(`Nid`, `Topic`, `Link`, `Source`, `DatePublish`, `DateStart`, `Cid_id`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])
f = codecs.open('intaff.txt','r','utf-8')
w = codecs.open('sqlIntaff.txt','w','utf-8')
sql = ""
for i in range(6,60):
	#sql = "INSERT INTO `news_news`(`Topic`, `Link`, `Source`, `DatePublish`, `Cid_id`) VALUES ('" +details[0]+"','"+details[1]+"','intaff','"+details[2]+"',1);"
	Sid = 0
	d120 = [6,17,18,25,31,32,33,37,38,42,45,47,50,51,52,53,54,56,57,58]
	d132 = [7,8,22,29,35,36,40,43,44,46]
	d140 = [9,10,11,12,13,14,15,16,19,20,21,23,24,26,27,28,34,39,49,55,59]
	if i in d120:
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+str(i)+",120);"
	elif i in d132:
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+str(i)+",132);"
	elif i in d140:
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+str(i)+",140);"
	w.write(sql+"\n")