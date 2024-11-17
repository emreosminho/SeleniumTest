from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib3.packages.six import BytesIO

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
username.send_keys("emreosman")

password = driver.find_element(By.ID, "password")
password.send_keys("123321")

loginButton = driver.find_element(By.CLASS_NAME, "radius").click()

result = driver.find_element(By.ID,"flash-messages").text

if "Your username is invalid!" in result:
    print("Kullanici adi hatali...")
else:
    print("Kullanici adi doğru...")


driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("123321")
driver.find_element(By.CLASS_NAME, "radius").click()
result = driver.find_element(By.ID, "flash-messages").text

if "Your password is invalid!" in result:
    print("Sifre hatali...")
else:
    print("Sifre dogru")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "radius").click()
result = driver.find_element(By.ID, "flash-messages").text

if "You logged into a secure area!" in result:
    print("Tebrikler Basarili Giris...")
else:
    print("Tekrar deneyiniz...")

driver.back()

print("**********************************************")

driver.get("https://the-internet.herokuapp.com/login")

def Login(username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "radius").click()
    result = driver.find_element(By.ID, "flash-messages").text
    return result


result = Login("asda", "123321")
if "Your username is invalid!" in result:
    print("Kullanici adi hatali...")
else:
    print("Kullanici adi doğru...")


result = Login("tomsmith","123321")
if "Your password is invalid!" in result:
    print("Sifre hatali...")
else:
    print("Sifre dogru")

result = Login("tomsmith","SuperSecretPassword!")
if "You logged into a secure area!" in result:
    print("Tebrikler Basarili Giris...")
else:
    print("Tekrar deneyiniz...")



driver.quit()