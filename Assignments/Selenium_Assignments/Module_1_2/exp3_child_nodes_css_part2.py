# EXPERIMENT TITLE: CHILD NODES USING CSS (Part 2 - Pattern Selectors)
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

    name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#name")))
    name_field.send_keys("Selenium Tester")
    print("CSS id selector -> Name field filled")

    date_fields = driver.find_elements(By.CSS_SELECTOR, "input[id^='date']")
    print(f"Elements whose id starts with 'date': {len(date_fields)}")
    for d in date_fields:
        print(" ->", d.get_attribute("id"))

    btn_elements = driver.find_elements(By.CSS_SELECTOR, "[id$='btn']")
    print(f"\nElements whose id ends with 'btn': {len(btn_elements)}")
    for b in btn_elements:
        print(" ->", b.get_attribute("id"), "| text:", b.text)

    table_elements = driver.find_elements(By.CSS_SELECTOR, "[id*='table' i]")
    print(f"\nElements whose id contains 'table': {len(table_elements)}")
    for t in table_elements:
        print(" ->", t.get_attribute("id"))

    day_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox'][id]")
    print(f"\nCheckboxes that have a non-empty id attribute: {len(day_checkboxes)}")
    for c in day_checkboxes:
        print(" ->", c.get_attribute("id"))
    time.sleep(2)
finally:
    driver.quit()
