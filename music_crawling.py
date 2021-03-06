import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
music_info = soup.select('div.music-list-wrap > table.list-wrap > tbody > tr > td.info')
rank = 1
for music in music_info:
        title = music.select_one('td.info >a.title.ellipsis').text
        title = title.strip()
        singer = music.select_one('td.info > a.artist.ellipsis').text
        print(rank, title, singer)
        rank += 1
