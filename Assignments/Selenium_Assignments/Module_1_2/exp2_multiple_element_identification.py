# EXPERIMENT TITLE: MULTIPLE ELEMENT IDENTIFICATION
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://testautomationpractice.blogspot.com/")
    wait = WebDriverWait(driver, 10)

    # 1) Find all <a> (link) elements on the page and print their text + href
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Total links found: {len(links)}\n")
    for index, link in enumerate(links, start=1):
        text = link.text.strip()
        href = link.get_attribute("href")
        if text:
            print(f"{index}. Text: '{text}' -> URL: {href}")

    # 2) Find all <input> elements and print their 'type' attribute
    print("\n--- Input field types on the page ---")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Total input elements found: {len(inputs)}")
    for i, inp in enumerate(inputs, start=1):
        print(f"{i}. type = {inp.get_attribute('type')}, id = {inp.get_attribute('id')}")

    # 3) Find all checkboxes and click each one
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    print(f"\nTotal checkboxes found: {len(checkboxes)}")
    for cb in checkboxes:
        if cb.is_displayed() and not cb.is_selected():
            driver.execute_script("arguments[0].scrollIntoView(true);", cb)
            cb.click()
    print("All visible checkboxes have been checked.")
    time.sleep(2)
finally:
    driver.quit()
