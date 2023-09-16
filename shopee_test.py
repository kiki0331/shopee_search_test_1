print("This is my homework")
import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "C:/Users/ASUS/Desktop/工作用/python/chromedriver-win32.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://shopee.tw/")
with open("456/cookie.json") as f:
    cookies = json.load(f)
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
time.sleep(5)
time.sleep(5)
search_xpath = "//input[@class ='shopee-searchbar-input__input']"
search = driver.find_element(By.XPATH,search_xpath)
search.clear()
search.send_keys("航海王")
time.sleep(5)
search_buttom_xpath = "//button[contains(@class ,'btn-solid-primary')]"
search_buttom = driver.find_element(By.XPATH,search_buttom_xpath)
search_buttom.click()
time.sleep(5)
product_xpath = "//div[@class ='FDn--+']"
product = driver.find_element(By.XPATH,product_xpath)
price_xpath = "//div[@class ='hpDKMN']"
price = driver.find_element(By.XPATH,price_xpath)

driver.close()
print("test")