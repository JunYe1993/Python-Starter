import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/Gossiping/index.html"
# url="https://tw.yahoo.com/"

request = requests.get(url)
content = request.content

file = open('result_01.txt', 'w', encoding='UTF-8')
file.write(content.decode('utf-8'))
file.close()
