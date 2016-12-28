# coding:utf-8
import urllib
import re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getAlbums(html):
    reg='"albummid":.*?"(.*?)",.*?"albumname":.*?"(.*?)".*?,'
    pattern = re.compile(reg, re.S)
    albums = re.findall(pattern, html)

    print "I have get the albums of this singer:", len(albums)
    for i in range(0, len(albums)):
        print i,"=",albums[i][0],albums[i][1]

html = getHtml("https://y.qq.com/portal/singer/0025NhlN2yWrP4.html#tab=album&")
#html = getHtml("https://y.qq.com/portal/singer/003Nz2So3XXYek.html#tab=album&")

getAlbums(html)







