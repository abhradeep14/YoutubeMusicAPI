from youtubesearchpython import VideosSearch
from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")
titles=[]
playid=ytmusic.get_playlist("PLd5ZrsVFhP8oxHt7ExLl55Qj-j46_8uix",limit=10)
tracks=playid["tracks"]
lentrack=len(tracks)
for x in range(0,lentrack):
   title=tracks[x]
   name=title['title']
   print(x, name)
   titles.append(name)

link=[]   

for i in range(0,lentrack):
 search=VideosSearch(titles[i],limit=1)
 result=(search.result())
 link_value = result['result'][0]['link']
 link.append(link_value)

import yt_dlp
ydl_opts = {
    'format': 'mp3/bestaudio/best',
}
for q in range(0,10):
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    download=ydl.download(link[q])
    print(q,titles[q])