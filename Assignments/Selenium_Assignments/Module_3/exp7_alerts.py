# EXPERIMENT TITLE: ALERTS
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
    time.sleep(2)

    # Simple Alert
    driver.find_element(By.XPATH, "//button[text()='Simple Alert']").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    print("Simple Alert:", alert.text)
    alert.accept()
    time.sleep(2)

    # Confirmation Alert
    driver.find_element(By.XPATH, "//button[text()='Confirmation Alert']").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    print("Confirmation Alert:", alert.text)
    alert.accept()
    time.sleep(2)

    # Prompt Alert
    driver.find_element(By.XPATH, "//button[text()='Prompt Alert']").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    print("Prompt Alert:", alert.text)
    alert.send_keys("Parthib")
    alert.accept()
    time.sleep(2)
finally:
    driver.quit()
