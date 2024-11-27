from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/Pc/Desktop/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("http://www.duckduckgo.com")
driver.maximize_window()

searchBox = driver.find_element(By.ID, "searchbox_input" )
searchBox.send_keys("vikipedi")
searchButton = driver.find_element(By.CLASS_NAME, "searchbox_iconWrapper__suWUe").click()
resultClick = driver.find_element(By.ID, "r1-1").click()


