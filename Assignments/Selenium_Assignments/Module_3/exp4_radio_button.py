# EXPERIMENT TITLE: RADIO BUTTON
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = ChromeOptions()
chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)

    radio1 = driver.find_element(By.XPATH, "//input[@value='radio1']")
    radio1.click()
    time.sleep(2)
    print("Radio 1 selected:", radio1.is_selected())
    time.sleep(3)
finally:
    driver.quit()
