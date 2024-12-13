from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/Pc/Desktop/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
seckin_madde_alani = driver.find_element(By.ID, "mp-tfa")
seckim_madde_yazisi = seckin_madde_alani.text
seckim_madde_yazisi = seckim_madde_yazisi.split(",")[0]
print("Seckin Madde: ", seckim_madde_yazisi)

kaliteli_madde = driver.find_element(By.ID, "mf-tfp").text.split(",")[0]
print("Kaliteli Maddesi: ", kaliteli_madde)

driver.quit()
