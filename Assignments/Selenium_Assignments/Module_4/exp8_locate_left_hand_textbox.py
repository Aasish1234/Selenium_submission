# EXPERIMENT TITLE: LOCATE THE LEFT-HAND SIDE TEXT BOX
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://text-compare.com/")
    driver.maximize_window()
    time.sleep(3)

    text_boxes = driver.find_elements(By.TAG_NAME, "textarea")
    left_box = text_boxes[0]
    left_box.click()
    left_box.send_keys("This is the left-hand side text box.")
    print("Left-hand side text box located successfully.")
    time.sleep(3)
finally:
    driver.quit()
