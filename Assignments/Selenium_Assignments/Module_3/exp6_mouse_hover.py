# EXPERIMENT TITLE: MOUSE HOVER
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = ChromeOptions()
chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
try:
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)

    mouse_hover = driver.find_element(By.ID, "mousehover")
    actions = ActionChains(driver)
    actions.move_to_element(mouse_hover).perform()
    time.sleep(3)
finally:
    driver.quit()
