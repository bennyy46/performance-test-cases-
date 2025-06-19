from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import time

def login_one_user():
    try:
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Wait for username field to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

        # ✅ Correct selectors based on Inspect tool
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        time.sleep(10000)
        driver.quit()
        return "✅ Login success"
    except Exception as e:
        return "❌ Login failed: " + str(e)

def test_many_users_login():
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(login_one_user) for _ in range(5)]
        for future in futures:
            results.append(future.result())
    return "Test Case 1 - Many Users Login Together:\n" + "\n".join(results)
