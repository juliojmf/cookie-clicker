from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

start_time = time.time()
timeout = start_time + 5*60 # time limit

chrome_driver_path = "" # your chrome driver path here
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

n = 1

while time.time() < timeout:
    cookie.click()
    if time.time() > start_time + 10*n: # time needed for checking the upgrades and buying the most expensive one
        n = n + 1
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")[::-1]
        for item in upgrades:
            try:
                item.click()
            except:
                pass

cookies_per_second = driver.find_element(By.ID, "cps").text
print(cookies_per_second)
