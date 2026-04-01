from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

url = "https://books.toscrape.com/"
title = []
price = []
round = 1

while True :
    print(f"round {round}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    products = soup.find_all('article',class_="product_pod")
    for product in products :
        title.append(product.find('h3').find('a').text)
        price.append(product.find('p',class_="price_color").text[2:])
        
    li_next = soup.find('li',class_="next")
    if li_next :
        url = url + li_next.find('a')['href']
        round = round + 1
        print(url)
    else :
        break
        

