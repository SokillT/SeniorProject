# -*- coding: utf-8 -*- 
import codecs

#INSERT INTO `news_news`(`Nid`, `Topic`, `Link`, `Source`, `DatePublish`, `DateStart`, `Cid_id`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])
f = codecs.open('2015-04-26 nisit.txt','r','utf-8')
t = codecs.open('types.txt','r','utf-8')
types = []
for i in t:
	i=i.strip('\n')
	types.append(i)
w = codecs.open('sqlNisit.txt','w','utf-8')
sql = ""
sid = 0
for i in f:
	i = i.strip('\n')
	line = i.split(',')
	#sql = "INSERT INTO `news_news`(`Nid`,`Topic`, `Link`, `Source`, `DatePublish`, `DateStart`, `Cid_id`) VALUES ('" +line[0]+ "','" +line[2]+ "','" +line[3]+ "','nisit.kasetsart.org','" +line[5]+ "','" +line[6]+ "','"+line[1]+"');"
	sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+line[0]+",210);"
	w.write(sql+"\n")
	if line[4]== types[0]:
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+line[0]+",217);"
	if line[4]== types[1]:
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+line[0]+",211);"
	if line[4]== types[2]:
		sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+line[0]+",216);"
	print sql
	w.write(sql+"\n")