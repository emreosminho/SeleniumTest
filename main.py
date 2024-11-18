import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/Users/Pc/Desktop/chromedriver-win64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("http://www.example.com")

link = driver.current_url
print("Su anki link: " + link)

baslik = driver.title

if baslik == "Examples":
    print("Su anki Baslik: "+ baslik)
else:
    print("Yanlis sayfadasiniz...")

driver.maximize_window()

driver.get("http://www.example.com")

driver.back()

time.sleep(2)

baslik = driver.title
if "Example" in baslik:
    driver.save_screenshot("./ekrangoruntusu.png")
else:
    print("Yanlis Sayfa...")

driver.quit()