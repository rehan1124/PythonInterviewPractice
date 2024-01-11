import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class AppLoadError(Exception):
    pass


URL = "https://demo.automationtesting.in/Windows.html"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get(URL)

current_window = driver.current_window_handle

try:
    driver.find_element(By.CSS_SELECTOR, "[id='Tabbed'] button[class='btn btn-inf']").click()

    handles = driver.window_handles
    print("Windows opened:", handles)
    for items in handles:
        driver.switch_to.window(items)
        print(driver.title)
except Exception:
    raise AppLoadError
finally:
    driver.switch_to.window(current_window)
    time.sleep(10)
    driver.quit()
