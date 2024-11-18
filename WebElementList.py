from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.imdb.com/")
driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
film_names = driver.find_elements(By.XPATH,"//ul/li//div[@class='ipc-metadata-list-summary-item__c']//a")

for film in film_names:
    print(film.text)

driver.quit()
