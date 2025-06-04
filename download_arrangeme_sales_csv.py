#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# --- Setup ---
email = "<email>"
password = "<password>"

options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment if you don't want the browser UI

driver = webdriver.Chrome(options=options)

try:
    # --- Step 1: Navigate to login page ---
    driver.get("https://www.arrangeme.com/account/signin")

    # --- Step 2: Enter credentials ---
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)

    # --- Step 3: Wait and go to Sales Reports page ---
    time.sleep(5)
    driver.get("https://www.arrangeme.com/account/dashboard#commissions")

    # --- Step 4: Wait and click download CSV ---
    time.sleep(5)
    download_button = driver.find_element(By.CSS_SELECTOR, "a.downloadSales")

    # Use JavaScript to click the element
    driver.execute_script("arguments[0].click();", download_button)

    #download_button = driver.find_element(By.CSS_SELECTOR, "a.downloadSales")
    #download_button.click()

    print("Download triggered. Check your default downloads folder.")

    # Wait to ensure download completes (you can make this smarter if needed)
    time.sleep(10)

finally:
    driver.quit()