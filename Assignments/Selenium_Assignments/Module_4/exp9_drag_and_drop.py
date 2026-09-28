# EXPERIMENT TITLE: DRAG AND DROP USING AUTOMATION
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    time.sleep(3)

    source = driver.find_element(By.XPATH, "//div[contains(text(), 'Drag me to my target')]")
    target = driver.find_element(By.XPATH, "//div[contains(text(), 'Drop here')]")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    time.sleep(3)
    print("Drag and drop operation completed successfully.")
finally:
    driver.quit()
