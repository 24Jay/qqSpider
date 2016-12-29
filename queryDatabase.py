#!/usr/bin/python
#-*-coding:utf8-*-

import MySQLdb

#open database and connect 
db = MySQLdb.connect(host='localhost',user='root', passwd='zhangjie',db='QQSpider',charset='utf8')

#get operation cursor
cursor = db.cursor()

sql = "SELECT id,name,state,songs,albums,mvs,followers FROM singers"

try:
    #execute sql
    cursor.execute(sql)

    #Get data
    results = cursor.fetchall()
    for row in results:
    	print row[0],row[1],row[2],row[3],row[4],row[5]
except:
    print("Error:unable to query the database!")

#close the connection
db.close()

