# EXPERIMENT TITLE: CHILD NODES USING CSS (Part 1 - Inspection)
# Name: Aasish Shrestha | Enrollment No: 12023002001003
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    def describe(label, by, value):
        try:
            el = driver.find_element(by, value)
            print(f"{label}: FOUND")
            print(f" tag='{el.tag_name}' id='{el.get_attribute('id')}' class='{el.get_attribute('class')}' ")
            parent = el.find_element(By.XPATH, "..")
            print(f" PARENT -> tag='{parent.tag_name}' id='{parent.get_attribute('id')}' class='{parent.get_attribute('class')}'")
        except Exception as e:
            print(f"{label}: NOT FOUND ({e.__class__.__name__})")
        print("-" * 70)

    describe("Point Me button", By.XPATH, "//*[contains(text(), 'Point Me')]")
    describe("Mobiles link", By.LINK_TEXT, "Mobiles")
    describe("Laptops link", By.LINK_TEXT, "Laptops")
    describe("Copy Text button", By.XPATH, "//*[contains(text(), 'Copy Text')]")
    describe("Static table", By.XPATH, "//table[.//td[contains(text(), 'Selenium')]]")
    time.sleep(3)
finally:
    driver.quit()
