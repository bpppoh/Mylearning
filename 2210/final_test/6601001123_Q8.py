from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

url_main = "https://books.toscrape.com/catalogue/"
url = url_main + "page-1.html"
title = []
price = []

while True :
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    products = soup.find_all('article',class_="product_pod")
    for product in products :
        title.append(product.find('h3').find('a').text)
        price.append(product.find('p',class_="price_color").text[2:])
        
    li_next = soup.find('li',class_="next")
    if li_next :
        url = url_main + li_next.find('a')['href']
    else :
        break
      
data = {
    "Book Title" : title ,
    "Price" : price
}

df = pd.DataFrame(data)
df.to_excel("books.xlsx",index=False)