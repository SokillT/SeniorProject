import codecs

f = codecs.open('sql.txt','w','utf-8')
news = codecs.open('nisit.txt','r','utf-8')

for i in news:
    new = i.split(',')
    f.write('INSERT INTO `news_news`(`Topic`, `Link`, `Cid`) VALUES ("'+new[0]+'","'+new[1].strip()+'",'+'2);\n')

#   INSERT INTO `News`(`id`, `Topic`, `Link`, `Category`) VALUES ([value-1],[value-2],[value-3],[value-4])

