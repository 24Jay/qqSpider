# -*- coding:utf-8 -*-
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getSongList(html):
    pattern = re.compile('<span.*?songlist__songname_txt"><a.*?>(.*?)</a></span>')
    songs = re.findall(pattern,html)
    print "I have get the songs of this album:" 
    print len(songs)
    for i in range(0,len(songs)):
    	print songs[i]
    

#html = getHtml("https://y.qq.com/portal/album/003DFRzD192KKD.html")
html = getHtml("https://y.qq.com/portal/album/0032ezFm3F53yO.html")
getSongList(html)
