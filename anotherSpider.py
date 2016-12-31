# -*- coding:utf-8 -*-

import urllib
import re
import MySQLdb

global count
count = 0
#######################################################################################
#get a html page based on the url
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#######################################################################################
#get the song list of a singer

def getSongList(html):
    pattern = re.compile('<span.*?songlist__songname_txt"><a.*?>(.*?)</a></span>')
    songs = re.findall(pattern, html)
    print "I have get the songs of this album:"
    print len(songs)
    for i in range(0, len(songs)):
        print songs[i]


#######################################################################################
#get a singer's detail
def getSinger(html):
    reg_3 = '<h1.*?class="data__name_txt js_index".*?title=.*?>(.*?)</h1>.*?<span.*?class="data_statistic__tit">(.*?)</span>.*?<strong.*?class="data_statistic__number">(.*?)</strong>'
    reg_2 = '<h1.*?class="data__name_txt js_index".*?title=.*?>(.*?)</h1>.*?<span.*?class="data_statistic__tit">(.*?)</span>.*?<strong.*?class="data_statistic__number">(.*?)</strong>.*?<span.*?class="data_statistic__tit">(.*?)</span><strong.*?class="data_statistic__number">(.*?)</strong>'
    reg_1 = '<h1.*?class="data__name_txt js_index".*?title=.*?>(.*?)</h1>.*?<span.*?class="data_statistic__tit">(.*?)</span>.*?<strong.*?class="data_statistic__number">(.*?)</strong>.*?<span.*?class="data_statistic__tit">(.*?)</span><strong.*?class="data_statistic__number">(.*?)</strong>.*?<span.*?class="data_statistic__tit">(.*?)</span><strong.*?class="data_statistic__number">(.*?)</strong>'
    pattern_1 = re.compile(reg_1,re.S)
    pattern_2 = re.compile(reg_2,re.S)
    pattern_3 = re.compile(reg_3,re.S)
    data = re.findall(pattern_1, html)
    print "Type(data) = ",len(data)
    if len(data) == 1:
        return data[0]
    print "Not find MV informations!!!!!!!!!!!!!!!!!!!!!!!!!"
    data = re.findall(pattern_2, html)
    if len(data) == 1:
        singer = data[0]+("MV","0")
        return singer
    print "Not find albums informations!!!!!!!!!!!!!!!!!!!!!!!!!"
    data = re.findall(pattern_3, html)
    singer = data[0] + ("专辑","0","MV", "0")
    return singer


def getAuthor(id):
    url = "https://y.qq.com/portal/singer/"+id+".html"
    print url
    html = getHtml(url)
    author = getSinger(html)
    return author

#######################################################################################
#The following codes will query the front page, and get the singer list.

def getSingerList(url):
    # url = 'https://y.qq.com/portal/singerlist.html'
    html = getHtml(url)
    reg ='<li.*?class="singer_list_txt__item"><a.*?href=.*?class="singer_list_txt__link js_singer".*?data-singermid="(.*?)".*?data-singerid=.*?title=.*?>(.*?)</a></li>'
    pattern = re.compile(reg,re.S)
    singerIDList = re.findall(pattern, html)
    return singerIDList

#######################################################################################
#THe following codes will do insertion operation
#open database and connect
def insertSinger(singerInfo):
    db = MySQLdb.connect(host='localhost',user='root', passwd='zhangjie',db='QQSpider',charset='utf8')
    #get operation cursor
    cursor = db.cursor()

    # SQL 插入语句

    name = singerInfo[1]
    state = "china"
    songs = int(singerInfo[2])
    albums = int(singerInfo[3])
    mvs = int(singerInfo[4])
    global count
    print count,name,state,songs,albums,mvs

    # # SQL 插入语句
    sql = "INSERT INTO singers(name,state,songs,albums,mvs,followers) VALUES ('%s', '%s', '%d','%d','%d','%s')" % (name,state,songs,albums,mvs,'100')
    try:
        #execute sql
        cursor.execute(sql)
        db.commit()
    except:
        print("Error:unable to query the database!")
    #close the connection
    db.close()
    print "Ennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnd"

def getPage(pageURL):
    global count
    singerList =getSingerList(pageURL)
    for singer in singerList:
        print "URL : ",singer[0],"      NAME ： ",singer[1]
    for singer in singerList:
        print "Starrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrt"
        author = getAuthor(singer[0])
        singerInfo = (count,author[0],author[2],author[4],author[6])
        insertSinger(singerInfo)
        count=count+1


for i in range(1,50):
    pageURL = "https://y.qq.com/portal/singerlist.html#t4="+str(i)+"&t3=all&t2=all&t1=all&"
    print pageURL
    getPage(pageURL)


