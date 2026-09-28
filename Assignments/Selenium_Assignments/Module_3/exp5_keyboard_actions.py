# EXPERIMENT TITLE: KEYBOARD ACTIONS
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = ChromeOptions()
chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)

    name = driver.find_element(By.ID, "name")
    name.send_keys("Parthib Kumar Das")
    time.sleep(2)

    name.send_keys(Keys.CONTROL, "a")
    time.sleep(2)

    name.send_keys(Keys.BACKSPACE)
    time.sleep(2)

    name.send_keys("Selenium Tester")
    time.sleep(3)
finally:
    driver.quit()
