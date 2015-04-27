# -*- coding: utf-8 -*- 
import codecs

#INSERT INTO `news_news`(`Nid`, `Topic`, `Link`, `Source`, `DatePublish`, `DateStart`, `Cid_id`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])
f = codecs.open('2015-04-26 engAnnounce.txt','r','utf-8')
w = codecs.open('sqlEng.txt','w','utf-8')
sql = ""
for i in f:
	i = i.strip('\n')
	line = i.split(',')
	sql = "INSERT INTO `news_news`(`Nid`,`Topic`, `Link`, `Source`, `DatePublish`, `Cid_id`) VALUES ('" +line[0]+ "','" +line[2]+ "','" +line[3]+ "','eng.ku.ac.th','" +line[4]+ "','"+line[1]+"');"
	#print sql
	w.write(sql+"\n")

	if line[1] == "2":
		print line[1]
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+line[0]+",220);"
		print sql
		w.write(sql+"\n")