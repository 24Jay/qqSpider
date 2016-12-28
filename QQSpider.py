#coding:utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getSongList(html):
    rrr = '<div.*?class="songlist__number">(.*?)</div>.*?<span.*?songlist__songname_txt">.*?<a.*?href="(.*?)".*?title=.*?>(.*?)</a></span>.*?<i.*?title=(.*?)></i>.*?<a.*?singer_name">(.*?)</a>.*?<div.*?songlist__time">(.*?)</div>'
    reg = '<div.*?class="songlist__number">(.*?)</div>'
    #Or use th following reg
    #reg = '<div.*?songlist__number">(.*?)</div>'

    #This point is raeally important, use compile(reg,re.S), then . can replace backspace.
    pattern = re.compile(rrr,re.S)
    songs = re.findall(pattern,html)
    print "I have get the songs of this album:",len(songs)
    print type(songs)
    for i in range(0,len(songs)):
        print songs[i][0],songs[i][1],songs[i][2],songs[i][3],songs[i][4],songs[i][5]

#html = getHtml("https://y.qq.com/portal/album/003DFRzD192KKD.html")
html = getHtml("https://y.qq.com/portal/album/0032ezFm3F53yO.html")
getSongList(html)


#output:
# I have get the songs of this album: 25
# <type 'list'>
# 1 //y.qq.com/portal/song/001JNb771zcCD3.html 以父之名 (Live) "独家" 周杰伦 05:59
# 2 //y.qq.com/portal/song/000vUML61Cw7Bw.html 止战之殇 (Live) "独家" 周杰伦 04:37
# 3 //y.qq.com/portal/song/002y5Eep0ddpnB.html 她的睫毛 (Live) "独家" 周杰伦 03:51
# 4 //y.qq.com/portal/song/001398Rf3gykz8.html 晴天 (Live) "独家" 周杰伦 04:59
# 5 //y.qq.com/portal/song/001EnnXb3RJLxb.html 你听得到 (Live) "独家" 周杰伦 03:49
# 6 //y.qq.com/portal/song/002LMVGv3aHgVC.html 梯田＋爸，我回来了 (Live) "独家" 周杰伦 04:36
# 7 //y.qq.com/portal/song/000BnfBg3PGbjt.html 园游会 (Live) "独家" 周杰伦 04:19
# 8 //y.qq.com/portal/song/000vm0CC2N5DvK.html 龙卷风 (Live) "独家" 周杰伦 04:08
# 9 //y.qq.com/portal/song/004KAi4m3qcmPl.html 将军 (Live) "独家" 周杰伦 03:02
# 10 //y.qq.com/portal/song/00362xJA4G7KdY.html 乱舞春秋 (Live) "独家" 周杰伦 04:35
# 11 //y.qq.com/portal/song/003OsAX54DdxDL.html 星晴 + 回到过去 + 最后的战役 + 爱我别走 (Live) "独家" 周杰伦 12:43
# 12 //y.qq.com/portal/song/001nLIIp3RPQ0X.html 我的地盘 (Live) "独家" 周杰伦 03:59
# 13 //y.qq.com/portal/song/003KO7cD0FkDFH.html 爱情悬崖 (Live) "独家" 周杰伦 04:22
# 1 //y.qq.com/portal/song/001d94K71ipdTB.html 搁浅 (Live) "独家" 周杰伦 04:21
# 2 //y.qq.com/portal/song/003wUZwx2ZF07d.html 借口 (Live) "独家" 周杰伦 04:21
# 3 //y.qq.com/portal/song/00125B4C0CzkIB.html 瓦解 (Live) "独家" 周杰伦 03:37
# 4 //y.qq.com/portal/song/0010CUSr4RyBE7.html 双刀＋双截棍＋龙拳 (Live) "独家" 周杰伦 07:00
# 5 //y.qq.com/portal/song/0027nQpk1l5zMk.html 困兽之斗 (Live) "独家" 周杰伦 04:23
# 6 //y.qq.com/portal/song/0023O1LH0Ha1OO.html 倒带 (Live) "独家" 周杰伦 04:36
# 7 //y.qq.com/portal/song/0022nw6P1dcHgp.html 简单爱 (Live) "独家" 周杰伦 06:33
# 8 //y.qq.com/portal/song/002ZKnKQ34rbZu.html 七里香 (Live) "独家" 周杰伦 05:02
# 9 //y.qq.com/portal/song/003JMGBC2DZsWK.html 外婆 (Live) "独家" 周杰伦 04:18
# 10 //y.qq.com/portal/song/0006yaTm0WDI7M.html 断了的弦 (Live) "独家" 周杰伦 04:50
# 11 //y.qq.com/portal/song/001BF0TR10z5R3.html 东风破 (Live) "独家" 周杰伦 05:14
# 12 //y.qq.com/portal/song/000zwjWq0T51ys.html 轨迹 (Live) "独家" 周杰伦 06:34