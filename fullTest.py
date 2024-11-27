import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from RadioButtonCheckBox import dropDown

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://tomspizzeria.b4a.app")
driver.maximize_window()

def siparisVer():
    driver.find_element(By.ID, "siparis").click()

def mesajOku():
    driver.find_element(By.ID, "mesaj").text


# müsteri ismi
siparisVer()
mesaj = mesajOku()
assert mesaj == "Müşteri ismi girmediniz"
# müsteri ismi girmediniz


driver.find_element(By.ID, "musteri-adi").send_keys("emreosminho")
siparisVer()
mesaj = mesajOku()
assert mesaj == "Pizza boyu sevmediniz"

driver.find_element(By.ID, "input[value='Küçük']").click()
siparisVer()
mesaj = mesajOku()
assert mesaj == "Ödeme tipi seçmediniz"

dropDown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropDown)
odeme.select_by_index(2)
siparisVer()
mesaj = mesajOku()
assert mesaj == "Siparişiniz alındı"



driver.execute_script("window.scrollBy(0,150)", "")
time.sleep(2)
driver.save_screenshot("./sonuc.png")
driver.quit()



