# EXPERIMENT TITLE: WEB ELEMENT IDENTIFICATION
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    print("=" * 70)
    print("INPUT ELEMENTS")
    print("=" * 70)
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, el in enumerate(inputs, start=1):
        print(f"{i}. id='{el.get_attribute('id')}' | name='{el.get_attribute('name')}' | type='{el.get_attribute('type')}' | placeholder='{el.get_attribute('placeholder')}'")

    print("\n" + "=" * 70)
    print("TEXTAREA ELEMENTS")
    print("=" * 70)
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    for i, el in enumerate(textareas, start=1):
        print(f"{i}. id='{el.get_attribute('id')}' | name='{el.get_attribute('name')}' | class='{el.get_attribute('class')}'")

    print("\n" + "=" * 70)
    print("SELECT (DROPDOWN) ELEMENTS")
    print("=" * 70)
    selects = driver.find_elements(By.TAG_NAME, "select")
    for i, el in enumerate(selects, start=1):
        print(f"{i}. id='{el.get_attribute('id')}' | name='{el.get_attribute('name')}'")
    time.sleep(3)
finally:
    driver.quit()
