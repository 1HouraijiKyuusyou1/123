import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
artical = soup.find_all("div", class_="r-ent")

data_list = []

for a in artical:
    data = {}
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "N/A"
    data["標題"] = title

    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date

    popularity = a.find("div", class_="nrec")
    if popularity and popularity.span:
        popularity = popularity.span.text
    else:
        popularity = "N/A"
    data["人氣"] = popularity

    data_list.append(data)

# 写入CSV文件
csv_file = 'ptt_nba_articles.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['標題', '日期', '人氣']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for data in data_list:
        writer.writerow(data)
