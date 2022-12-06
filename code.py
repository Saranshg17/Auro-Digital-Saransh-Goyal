import pandas as pd
from bs4 import BeautifulSoup

book1 = []
book2 = []
book3 = []

with open('orders.xml', 'r') as f:
	data = f.read()

data = data.split(">")

for tr in data:
    tr=tr.split(" ")
    if tr[0] == "<AddOrder" :
        book=tr[1].split("=")[1]
        op=tr[2].split("=")[1]
        pr=tr[3].split("=")[1]
        vol=tr[4].split("=")[1]
        print(book)

        if book[1:7]=="book-1":
            book1.append({
                op:vol+"@"+pr
            })
        elif book[1:7]=="book-2":
            book2.append({
                op:vol+"@"+pr
            })
        elif book[1:7]=="book-3":
            book3.append({
                op:vol+"@"+pr
            })

df1 = pd.DataFrame(book1)
df1 = df1.replace('\n','', regex=True)
df2 = pd.DataFrame(book2)
df2 = df2.replace('\n','', regex=True)
df3 = pd.DataFrame(book3)
df3 = df3.replace('\n','', regex=True)
print(df1)


