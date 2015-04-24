import MySQLdb
import codecs
from datetime import datetime


sql = "INSERT INTO `news_news`(Topic,Link) VALUES ("
topic=codecs.open('intaff.txt','r','utf-8')
f = codecs.open('sql.txt','w','utf-8')
i = 0
for line in topic:
	i=i+1
	print i
	sline = line.split(',')
	sqls = sql + "'" + sline[0]+ "','"+sline[1]+"');"
	f.write(sqls+"\n")

f.close()
