import urllib2
from bs4 import BeautifulSoup
import sys
from urllib import urlretrieve
reload(sys)

def imgGreb():
    site_url = "http://www.ku.ac.th/web2012/index.php?c=adms&m=mainpage1"
    html = urllib2.urlopen(site_url).read()
    soup = BeautifulSoup(html)
    print soup
    #url = "http://www.ku.ac.th/web2012/resources/upload/content/1429686096_img.jpg"
    url = "http://www.ku.ac.th/web2012/"
    
    img=soup.findAll(['img'])
    
    
    for i in img:
        try:
			url = "http://www.ku.ac.th/web2012/"
            # built the complete URL using the domain and relative url you scraped
			url = url + i.get('src')
            # get the file name 
			name = "./img/" +url.split('/')[-1] 
            # detect if that is a type of pictures you want
			type = name.split('.')[-1]
			if type in ['jpg', 'png', 'gif']:
                # if so, retrieve the pictures
				urlretrieve(url, name)
        except:
			pass

if __name__ == '__main__':
    imgGreb()
