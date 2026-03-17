from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument("--window-size=1920,1080")
driver.get("https://www.lotuss.com/th")
searchBox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"search-bar-input"))
)
searchBox.send_keys("น้ำดื่มตราสิงห์")
searchBox.send_keys(Keys.ENTER)

WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "product-grid-item")) 
)
last_height = driver.execute_script("return document.body.scrollHeight")
while True :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height :
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source,'html.parser')
name = []
price = []
for item in soup.find_all('div',class_="product-grid-item") :
    name.append(item.find('p').get_text())
    price.append(item.find('div',class_="mui-style-18s6ztp").get_text())

# input("")
# driver.quit()
print("Copying to excel...")
data = {
    'Product Name' : name ,
    'Price' : price
}
df = pd.DataFrame(data)
df.to_excel("result_Lab10.xlsx",index=False)
