import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://tomspizzeria.b4a.app/")

middle = driver.find_element(By.CSS_SELECTOR, "input[value='Orta']")
zeytin = driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']")
print(middle.is_selected())
print(zeytin.is_selected())
middle.click()
zeytin.click()
print(middle.is_selected())
print(zeytin.is_selected())

print("******************************")

dropDown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropDown)
odeme_tipleri = odeme.options

for tip in odeme_tipleri:
    print(tip.text)

time.sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
time.sleep(2)
odeme.select_by_index(2)
time.sleep(2)
driver.quit()







