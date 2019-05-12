import sys
import requests
from bs4 import BeautifulSoup

url="https://www.youtube.com/feed/trending/"

request = requests.get(url)
content = request.content

soup = BeautifulSoup(content,"html.parser")
container = soup.select("h3 a")

# print(type(container))
# print(container)
# 接下來只是寫入result.txt檔案的事情
file = open('result_02.txt', 'w', encoding='UTF-8')
for item in container:
     if item:
          value = item.get_text()
          print(value)
          file.write(value+'\n')
          #break #這裡也提一個起手式的遺珠之憾，就是你可以用continue和break來處理 迴圈敘述，這裏為了我之前debug方便，使用break來讓我先只看一個的結果。
file.close()