import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
quotes = []
authors = []

while url :
    print(f"Directed to {url}")
    response = requests.get(url)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text,'html.parser')
        quote_div = soup.find_all('div',class_="quote")
        for item in quote_div :
            quotes.append(item.find('span',class_="text").string)
            authors.append(item.find('small',class_="author").string)
        next_li = soup.find('li',class_="next")
        if next_li :
            next_href = next_li.find('a')['href']
            if next_href :
                url = "https://quotes.toscrape.com" + next_href
            else :
                url = ""
        else :
            url = ""
    else :
        print("response is null ")
        url = ""
        
if len(quotes) != 0 and len(authors) != 0 :
    print("Copying to excel...")
    data = {
        'Author' : authors ,
        'Quote' : quotes
    }
    df = pd.DataFrame(data)
    df.to_csv("result_Lab9.csv",index=False)
else :
    print("Quotes List or Authors List is empty")