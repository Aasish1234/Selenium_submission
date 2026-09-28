# EXPERIMENT TITLE: WRITE TEXT IN THE BOX
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    time.sleep(3)

    name_box = driver.find_element(By.ID, "name")
    name_box.send_keys("Parthib Kumar Das")
    print("Text entered successfully.")
    time.sleep(3)
finally:
    driver.quit()
