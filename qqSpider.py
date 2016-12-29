# -*- coding:utf-8 -*-

import urllib
import re
import MySQLdb

#######################################################################################
#######################################################################################
#get a html page based on the url
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#######################################################################################
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
#######################################################################################
#get a singer's detail
def getSinger(html):
    reg = '<h1.*?class="data__name_txt js_index".*?title=.*?>(.*?)</h1>.*?<span.*?class="data_statistic__tit">(.*?)</span>.*?<strong.*?class="data_statistic__number">(.*?)</strong>.*?<span.*?class="data_statistic__tit">(.*?)</span><strong.*?class="data_statistic__number">(.*?)</strong>.*?<span.*?class="data_statistic__tit">(.*?)</span><strong.*?class="data_statistic__number">(.*?)</strong>'
    pattern =re.compile(reg,re.S)
    data = re.findall(pattern, html)
    print "Information about the singer:", len(data[0])
    for singer in data:
        print type(singer)
        print singer[0],singer[1],singer[2],singer[3],singer[4],singer[5],singer[6]
    return singer

def getAuthor(id):
    url = "https://y.qq.com/portal/singer/"+id+".html"
    print url
    html = getHtml(url)
    author = getSinger(html)
    print author
    return author

#getAuthor("0025NhlN2yWrP4")

#######################################################################################
#######################################################################################
#######################################################################################
#The following codes will query the front page, and get the singer list.

def getSingerList():
    url = 'https://y.qq.com/portal/singerlist.html'
    html = getHtml(url)
    reg ='<h3.*?class="singer_list__title"><a.*?href=.*?data-singermid="(.*?)".*?data-id=.*?class=.*?title=.*?>(.*?)</a>.*?</h3>'
    pattern = re.compile(reg,re.S)
    singerIDList = re.findall(pattern, html)
    print "The size of the singlist: ", len(singerIDList)
    for singer in singerIDList:
        print singer[0],singer[1]
    return singerIDList

#print getSingerList()



#######################################################################################
#######################################################################################
#THe following codes will do insertion operation
#open database and connect
def insertSinger(singerInfo):
    db = MySQLdb.connect(host='localhost',user='root', passwd='zhangjie',db='QQSpider',charset='utf8')
    #get operation cursor
    cursor = db.cursor()

    # SQL 插入语句

    id = singerInfo[0]
    name = singerInfo[1]
    state = "china"
    songs = int(singerInfo[2])
    albums = int(singerInfo[3])
    mvs = int(singerInfo[4])

    print id,name,state,songs,albums,mvs

    # # SQL 插入语句
    sql = "INSERT INTO singers(id,name,state,songs,albums,mvs,followers) VALUES ('%d', '%s', '%s', '%d','%d','%d','%s')" % (id,name,state,songs,albums,mvs,'100')
    try:
        #execute sql
        cursor.execute(sql)
        db.commit()
        print "hhhhhhhhhhhhhhhhhhhhhhh"
    except:
        print("Error:unable to query the database!")
    #close the connection
    db.close()
print "################################3"
singerList =getSingerList()
count =10
for singer in singerList:
    author = getAuthor(singer[0])
    print "作者信息长度：",len(author)
    for i in range(0,len(author)):
        print author[i]
    singerInfo = (count,author[0],author[2],author[4],author[6])
    insertSinger(singerInfo)
    count=count+1

