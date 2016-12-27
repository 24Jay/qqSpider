#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getSongList(html):
    reg = r'title="(.+?)">'

    regg = r'span"(.+?)"span'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print "hhhhhhhhhhhhhhhhhhhh"
    print imglist

html = getHtml("https://y.qq.com/portal/album/001OQeBY0DrWj0.html#")
print html
getImg(html)