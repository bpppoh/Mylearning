from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://quotes.toscrape.com/login"

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)

usernameBox = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"username"))
)
passwordBox = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"password"))
)
loginBtn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME,"btn"))
)
usernameBox.send_keys("comsci")
passwordBox.send_keys("password")
time.sleep(2)
loginBtn.send_keys(Keys.ENTER)
WebDriverWait(driver,10).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME,"quote"))
)
time.sleep(1)
driver.quit()