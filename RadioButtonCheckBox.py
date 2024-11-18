from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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






