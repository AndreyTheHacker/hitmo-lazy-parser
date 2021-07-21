import requests as r
import subprocess as sp

def searchmusic(query):
    q = r.get("https://rum.hotmo.org/search?q="+query.replace(" ","+")).text
    q = q[q.find('<div class="p-info p-inner">'):]
    q = q[q.find('<ul class="tracks__list">'):]
    q=q.split("href=")
    w = []
    for i in q:
        if(i.startswith('"http')):
            k=i[1:]
            k=k[:k.find('"')]
            if k.find("/get/")>-1:
                w.append(k)
    return w

def getmusicbyurl(url):
    q = r.get(url).text
    q=q[q.find('<div class="tracks__item track mustoggler"')+42:]
    q=q[q.find('<a data-nopjax')+14:]
    q=q[q.find('href="')+6:]
    return q[:q.find('"')].replace("\\","")

tracks = searchmusic(input("Search: "))
for i in tracks:print(i)
a = input("Choose [%d-%d]: "%(0,len(tracks)-1))
b = input("Select player [mpv]: ")
if b=="": b="mpv"
sp.call([b,tracks[int(a)]])