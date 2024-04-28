import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url)    # 取得網頁內容
web.encoding='utf-8'       # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

soup = BeautifulSoup(web.text, "html.parser")                    # 轉換成標籤樹
td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]

data = {
    "特別獎": [ns, '', ''],
    "特獎": [n1, '', ''],
    "頭獎": n2,
    "二獎": [n2[0][-7:], n2[1][-7:], n2[2][-7:]],
    "三獎": [n2[0][-6:], n2[1][-6:], n2[2][-6:]],
    "四獎": [n2[0][-5:], n2[1][-5:], n2[2][-5:]],
    "五獎": [n2[0][-4:], n2[1][-4:], n2[2][-4:]],
    "六獎": [n2[0][-3:], n2[1][-3:], n2[2][-3:]]
}

df = pd.DataFrame(data)
df = df.T
df["獎金"] = [10000000, 2000000, 200000, 40000, 10000, 4000, 1000, 200]
print(df)

df.to_csv("Lottery Number_113_Jan_Feb.csv")